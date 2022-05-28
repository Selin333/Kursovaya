import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from platform import python_version

import imaplib
import email


def pochta_otpravka():
    try:

        server = 'smtp.yandex.ru'
        user = 'mail4studying@yandex.ru'
        password = 'endga34nogam44543421'

        recipients = ['danyamelman@yandex.ru']
        sender = 'mail4studying@yandex.ru'
        subject = 'Тема сообщения'
        text = 'Текст сообщения'
        html = '<html><head></head><body><p>' + text + '</p></body></html>'

        filepath = "D:\\111\\file.txt"
        basename = os.path.basename(filepath)
        filesize = os.path.getsize(filepath)

        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = 'Python script <' + sender + '>'
        msg['To'] = ', '.join(recipients)
        msg['Reply-To'] = sender
        msg['Return-Path'] = sender
        msg['X-Mailer'] = 'Python/' + (python_version())

        part_text = MIMEText(text, 'plain')
        part_html = MIMEText(html, 'html')
        part_file = MIMEBase('application', 'octet-stream; name="{}"'.format(basename))
        part_file.set_payload(open(filepath, "rb").read())
        part_file.add_header('Content-Description', basename)
        part_file.add_header('Content-Disposition', 'attachment; filename="{}"; size={}'.format(basename, filesize))
        encoders.encode_base64(part_file)

        msg.attach(part_text)
        msg.attach(part_html)
        msg.attach(part_file)

        mail = smtplib.SMTP_SSL(server)
        mail.login(user, password)
        mail.sendmail(sender, recipients, msg.as_string())
        mail.quit()
        print('Письмо отправлено')
    except:
        print('error')
# pochta_otpravka()
