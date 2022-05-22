import smtplib, ssl
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send(receiver_address, subject, content):
    sender_adress = "your.email.adress@gmail.com" # <--------- Type your adress email (sender) 
    # if you store credentials as env variables 
    # password = os.environ['EMAIL_CRED']
    with open('password.txt', 'r') as f:
        password = f.read()
    if password =='':
        print('The password.txt file is empty. It should contain your your-16-digit-password')
        return 0

    try:
        # Setup the MIME
        message = MIMEMultipart()
        message['From'] = sender_adress
        message['To'] = receiver_address
        message['Subject'] = subject
        message.attach(MIMEText(content, 'plain'))

        # Create SMPT session for sending the mail
        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.ehlo()  # check connection
        session.starttls()
        session.ehlo()  # check connection
        session.login(sender_adress, password)
        text = message.as_string()
        session.sendmail(sender_adress, receiver_address, text)
        session.quit()
        print('Mail Sent')
        return 0
    except Exception as e:
        print(e)
        return 0 
############################################################
if __name__ == '__main__':
    receiver_address = 'receiver@abc.ef' # <--------- Type the adress email of receiver 
    subject = 'Subject of email - test email' # <--------- Type the subject of email
    content = 'Content of message - test mail' # <--------- Type the content of email

    send(receiver_address, subject, content)