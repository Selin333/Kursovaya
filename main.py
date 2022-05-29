import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from platform import python_version

import imaplib
import email
from PyQt5.QtWidgets import QMessageBox, QVBoxLayout, QLabel
from PyQt5 import QtWidgets
from PyQt5.QtWinExtras import QtWin
from PyQt5.QtWidgets import QDialog, QPushButton, QApplication


myappid = 'kursach'
QtWin.setCurrentProcessExplicitAppUserModelID(myappid)
from GUI import Ui_MainWindow  # импорт ui
import sys


def Error(info):
    error = QMessageBox()
    error.setIcon(QMessageBox.Critical)
    error.setText("Ошибка")
    error.setInformativeText(info)
    error.setWindowTitle("Ой-йой")
    error.exec_()
class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_3.clicked.connect(self.btnClicked)
        self.ui.pushButton_4.clicked.connect(self.btnClicked_2)
        self.ui.pushButton_5.clicked.connect(self.btnClicked_5)



    def btnClicked_5(self):
        import PyQt5
        global filepath

        filepath = PyQt5.QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', 'D:\\111\\Kursovaya', 'txt file(*.txt)')

    def btnClicked(self):
        if not 'filepath' in globals() :
            Error('файл не выбран')
        elif len(filepath[0]) == 0:
            Error('файл не выбран')
        else:

            server = self.ui.lineEdit.text()
            user = self.ui.lineEdit_2.text()
            password = self.ui.lineEdit_3.text()
            recipients = self.ui.lineEdit_4.text()
            subject = self.ui.lineEdit_5.text()
            text = self.ui.lineEdit_6.text()
            if len(server) ==0 or len(user) ==0 or len(password) ==0 or len(recipients) ==0 or len(subject) ==0 or len(text) ==0:

                Error('Заполните все поля')
            else:
                print('good')

                pochta_otpravka(server, user, password, recipients, subject, text, filepath[0])


    def btnClicked_2(self):
        mail_imap = self.ui.lineEdit_7.text()
        mail_login = self.ui.lineEdit_8.text()
        mail_passwd = self.ui.lineEdit_9.text()
        if len(mail_imap) == 0 or len(mail_login) == 0 or len(mail_passwd) == 0:
            Error('Заполните все поля')
        else:
            print('zzzzz')
        pochta_read(mail_imap,mail_login,mail_passwd)


def pochta_otpravka(server,user,password,recipients,subject,text,filepath):
    try:

        sender = user

        html = '<html><head></head><body><p>' + text + '</p></body></html>'

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
        Error('не правильно заполнены поля'
        )
def pochta_read(mail_imap,mail_login,mail_passwd):
    try:

        mail = imaplib.IMAP4_SSL(mail_imap)
        mail.login(mail_login, mail_passwd)

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
    except:
        Error('не правильно заполнены поля'
        )



app = QtWidgets.QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec())