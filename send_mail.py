import smtplib
from email.mime.text import MIMEText


def send_mail(name,email,comment):
    port=2525
    smtp_server= 'smtp.mailtrap.io'
    login = '1e63bfd284e93a'
    password ='abe557ad78db90'
    message=f"<h3>New Feedback submission </h3><ul><li>Name:{name}</li><li>Email:{email}</li><li>message:{comment}</li></ul>"

    sender_emai='email1@example.com'
    receiver_email='email2@example.com'
    msg = MIMEText(message,'html')
    msg['Subject']='Application Feedback'
    msg['From']=sender_emai
    msg['To']= receiver_email

    #send_email
    with smtplib.SMTP(smtp_server,port) as server:
        server.login(login,password)
        server.sendmail(sender_emai,receiver_email,msg.as_string())
