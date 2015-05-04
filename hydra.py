import smtplib
import time

while True:

    gmail_user = 'max@robobox.net'
    gmail_pwd = 'Game0fthr0ne$'
    smtpserver = smtplib.SMTP("box560.bluehost.com",26)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(gmail_user, gmail_pwd)

    with open('emails.txt','r') as conn:

        for x in conn.readlines():

            to = x.strip('\n')
            header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:testing \n'
            msg = header + '\n Someone call the olympics and tell them to cancel 2016. I already won. \n\n'
            try:
            	smtpserver.sendmail(gmail_user, to, msg)
            except:
            	pass

        print 'done!'
        smtpserver.close()
        time.sleep(3600)

