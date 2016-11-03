require 'net/http'
require 'net/smtp'
require 'uri'
require 'nokogiri'

_IDENTIFIERTYPE = '1'
_IDENTIFIER = 'NNNNNNNN'
_SURNAME = 'XXXXXX'
_DOB = 'YYYY-MM-DD'

sender = 'yourname@company.com'
receiver = 'yourname@company.com'
smtpServer = 'SMTP.company.com'

_BaseURL = 'https://services3.cic.gc.ca/ecas/'
_URL0 = 'authenticate.do'

uri = URI(_BaseURL + _URL0)
http = Net::HTTP.new(uri.host, uri.port)
http.use_ssl = true

# GET request -> so the host can set his cookies
resp = http.get(uri.path, nil)
cookie = resp.response['set-cookie'].split('; ')[0]

# POST request -> logging in
data = 'lang=&_page=_target0&app=&identifierType=' + _IDENTIFIERTYPE + '&identifier=' + _IDENTIFIER + '&surname=' + _SURNAME + '&dateOfBirth=' + _DOB + '&countryOfBirth=202&_submit=Continue'
headers = {
    'Cookie' => cookie,
    'Referer' => _BaseURL + _URL0,
    'Content-Type' => 'application/x-www-form-urlencoded'
}
resp = http.post(uri.path, data, headers)

# Extract Redirect URL
$_URL1 = ''
resp.each { |key, value|
  if key == 'location' then
    $_URL1 = value
  end }

# POST request -> so we can get details link
uri = URI($_URL1)
resp = http.post(uri.path, data, headers)
$_URL2 = ''
resp.body.each_line { |line|
  if line.include? 'viewcasehistory.do'
    $_URL2 = (line.split("=\""))[1].split("\">")[0].gsub(/&amp;/, '&')
  end
}

# POST request -> for final result
uri = URI(_BaseURL + $_URL2)
data = $_URL2.split('?')[1]
resp = http.post(uri.path, data, headers)

=begin
# DEBUG ONLY
TEMPstr = IO.read("./OUTPUT")
puts TEMPstr.length;
=end

html_doc = Nokogiri::HTML(resp.body)
$_Result = ''
html_doc.css('li').each do |link|
  if "#{link['class']}" == 'margin-bottom-medium'
    $_Result += "#{link.content}\n"
  end
end

puts 'Current query result length is ' + $_Result.length.to_s + ", modify following condation if necessary.\n"
puts $_Result

#message = ''
message = "From: Your Name <" + sender + ">\n"
message += "To: Your Name <" + receiver + ">\n"
message += "Subject: Application Status as of " + Time.new.strftime("%Y-%m-%d %H:%M")+ "\n\n"
message += $_Result

Net::SMTP.start(smtpServer) do |smtp|
  smtp.send_message message, sender, receiver
end
