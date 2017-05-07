from sheard.SmtpMailer import SmtpMailer

if __name__ == '__main__':
    smtp = SmtpMailer('', '')
    smtp.message_builder().with_from('').with_to('').with_subject('').with_text_attach('').send()
    smtp.quit()
