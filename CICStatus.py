#!/usr/bin/env python

import urllib2, urllib, re, smtplib, datetime, time, random, cookielib
from cookielib import CookieJar
from HTMLParser import HTMLParser
from email.mime.text import MIMEText
from email.header import Header

IDENTIFIER = 'nnnnnnnnn'
SURNAME = 'XXXXXX'
DOB = 'YYYY-MM-DD'

Sender = 'yourname@company.com'
Receiver = 'yourname@company.com'
SMTPServer = 'company.com'
Subject = 'Application Status as of ' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

Result = ''

BaseURL = 'https://services3.cic.gc.ca/ecas/'
URL0 = 'authenticate.do'

class hp(HTMLParser):
    a_text = False

    def handle_starttag(self, tag, attr):
        if tag == 'li':
            if len(attr) == 0: pass
            else:
                for (variable, value) in attr:
                    if variable == "class" and value == "margin-bottom-medium":
                        self.a_text = True

    def handle_endtag(self, tag):
        if tag == 'li':
            self.a_text = False

    def handle_data(self, data):
        global Result
        if self.a_text and len(data.strip()) > 0:
            Result = Result + data.strip() + '\n'

# Get Cookie
Cookie = cookielib.CookieJar()
Opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(Cookie))
Response = Opener.open(BaseURL + URL0)
time.sleep(random.randint(3, 8))

# Login to view Application Status, and get Application Details URL
Request = urllib2.Request(BaseURL + URL0)
#Opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(Cookie))
FormData = { "lang": "", "_page": "_target0", "app": "", "identifierType": "1", "identifier": IDENTIFIER, "surname": SURNAME, "dateOfBirth": DOB, "countryOfBirth": "202", "_submit": "Continue" }
DataEncoded = urllib.urlencode(FormData)
Response = Opener.open(Request, DataEncoded)
Content = Response.read()
URL1 = re.search('viewcasehistory.do.*lang=en', Content).group(0).replace("&amp;", "&")
time.sleep(random.randint(3, 8))

# View Application Details by access URL1
#Opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(Cookie))
Response = Opener.open(BaseURL + URL1)
Content = Response.read()

# HTML Parser
Output = hp()
Output.feed(Content)
Output.close()

print Result

MSG = MIMEText(Result, 'text', 'utf-8')
MSG['Subject'] = Header(Subject, 'utf-8')

SMTP = smtplib.SMTP()
#smtp.set_debuglevel(1)
SMTP.connect(SMTPServer)
SMTP.sendmail(Sender, Receiver, MSG.as_string())
SMTP.quit()
