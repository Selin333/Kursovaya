import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from platform import python_version
from email.header import decode_header

import imaplib
import email


def pochta_otpravka():
    try:

        server = 'smtp.yandex.ru'
        user = 'mail4studying@yandex.ru'
        password = 'endga34nogam44543421'

        recipients = ['danyamelman@yandex.ru']
        sender = user
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
pochta_otpravka()
def pochta_read():
    mail = imaplib.IMAP4_SSL('imap.yandex.ru')
    mail.login('danyamelman@yandex.ru', 'roHB5m8kmy9sdKUm52QoAX2')

    mail.list()
    mail.select("inbox")
    result, data = mail.search(None, "ALL")

    ids = data[0]
    id_list = ids.split()
    latest_email_id = id_list[-1]

    result, data = mail.fetch(latest_email_id, "(RFC822)")
    raw_email = data[0][1]
    raw_email_string = raw_email.decode('utf-8')

    email_message = email.message_from_string(raw_email_string)
    # print(email_message)
    print(email_message['To'])
    print(email.utils.parseaddr(email_message['From']))
    print(email_message['Date'])


    email_message = email.message_from_string(raw_email_string)
    content_email = []
    if email_message.is_multipart():
        for payload in email_message.get_payload():
            body = payload.get_payload(decode=True).decode('utf-8')
            content_email.append(body)
            print(body)
    else:
        body = email_message.get_payload(decode=True).decode('utf-8')
        print(body)
    print(content_email)

pochta_read()