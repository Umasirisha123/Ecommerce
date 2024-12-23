import smtplib
from smtplib import SMTP
from email.message import EmailMessage

def sendmail(to,subject,body):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('umasirishathotakura2002@gmail.com','xego oest tgul errx')
    msg=EmailMessage()
    msg['From']='umasirishathotakura2002@gmail.com'
    msg['Subject']=subject
    msg['To']='thotakuraumasirisha123@gmail.com'
    msg.set_content(body)
    server.send_message(msg)
    server.quit()