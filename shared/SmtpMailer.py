import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class SmtpMailer:
    def __init__(self, user, password):
        self.smtp = smtplib.SMTP(host='smtp.gmail.com', port=25)
        self.smtp.starttls()
        self.smtp.login(user, password)

    def message_builder(self):
        self.currentMessage = MIMEMultipart()
        return self

    def with_from(self, from_user):
        self.currentMessage['From'] = from_user
        return self

    def with_to(self, to):
        self.currentMessage['To'] = to
        return self

    def with_subject(self, subject):
        self.currentMessage['Subject'] = subject
        return self

    def with_text_attach(self, text):
        self.currentMessage.attach(MIMEText(text, 'plain'))
        return self

    def send(self):
        self.smtp.send_message(self.currentMessage)
        del self.currentMessage

    def quit(self):
        self.smtp.quit()
