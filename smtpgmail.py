import smtplib
from email.mime.text import MIMEText

gmail_user = 'youtgmail'
gmail_password = 'yourapppass'

smtp_login_mail = "from@samplefrom.com"
sent_from = "From Name"
to = ['to@sample.com']

msg = MIMEText('Your body Message here')
msg['Subject'] = 'email subject'
msg['From'] = sent_from + ' <' + smtp_login_mail + '>'
msg['To'] = 'to@sample.com'

try:  
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, msg.as_string())
    server.close()

    print('Email sent!')

except:  
    print('Something went wrong...')