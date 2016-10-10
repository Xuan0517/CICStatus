## Overall
While your application was processed by CIC, you can use your UCI or Application number query your application status. Basically you have to do it via browser, access CIC website, input your login information include UCI number, your surname, and DOB/POB. It need your manual operation, this script can perform the query operation automatically and send the query result to you by email (if necessary)

## Key Features
 1. Scheduled by system job monitor or start manually
 2. Query status and output to console
 3. Send query result by email
 4. Support query by Applicaiton number, UCI number, Receipt number
 5. Easy to use
 6. ...

## Modify key/value in script
Open CICStatus.py with any text editor, modify the following values

Key                             | Description
--------------------------------|----------------------------------------------------------------------------
**IDENTIFIER**                  | Your UCI number, or Application number
**SURNAME**                     | Your surname
**DOB**                         | Your DOB
**POB**                         | Set to '202' by default, if you are not born in China, change to other value
--------------------------------|----------------------------------------------------------------------------
**Sender**                      | Sender email address
**Receiver**                    | Receiver email address
**SMTPServer**                  | Your SMTP server

## Prerequisite:
 - Python version 2.6 or higher
   - Download Python from [this page ] (https://www.python.org/downloads/), currently it support Windows, Mac and Linux

## Steps
###Clone project
```
MBP:~ Xuan$ git@github.com:Xuan0517/CICStatus.git
```
Or access https://github.com/Xuan0517/CICStatus usieng browser and click 'Clone or download', then click 'Download ZIP', unpack the downloaded ZIP file to any folder
###Check prerequisite
```
MBP:~ Xuan$ python -V
Python 2.7.5
```

###Run
```
MBP:~ Xuan$ python CICStatus.py
```

## TODO
 - Add other query type
 - ...

*This is not a part of any product. You are not allowed to share this script to others (include but not limited Scripts and Textfiles), the author may have patents or pending patent applications covering subject matter described in this documentation. The furnishing of this utility does not give you any license to these patents.*