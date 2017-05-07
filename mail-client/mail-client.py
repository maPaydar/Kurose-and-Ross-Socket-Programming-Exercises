import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_mail(their_address, message):
    s = smtplib.SMTP(host='smtp.gmail.com', port=25)
    s.starttls()
    s.login('mapsgp920@gmail.com', '')
    msg = MIMEMultipart()
    msg['From'] = 'mapsgp920@gmail.com'
    msg['To'] = their_address
    msg['Subject'] = "I Love u"
    msg.attach(MIMEText(message, 'plain'))
    s.send_message(msg)
    del msg
    s.quit()
    return

send_mail('mapsgp920@gmail.com', 'I Love u baby')
