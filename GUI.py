# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1058, 747)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 10, 1041, 691))
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(120, 470, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(400, 480, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab)
        self.tabWidget_2.setGeometry(QtCore.QRect(0, -40, 1041, 691))
        self.tabWidget_2.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget_2.setUsesScrollButtons(True)
        self.tabWidget_2.setDocumentMode(False)
        self.tabWidget_2.setTabsClosable(False)
        self.tabWidget_2.setMovable(False)
        self.tabWidget_2.setTabBarAutoHide(False)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_10 = QtWidgets.QWidget()
        self.tab_10.setObjectName("tab_10")
        self.tabWidget_2.addTab(self.tab_10, "")
        self.tab_11 = QtWidgets.QWidget()
        self.tab_11.setObjectName("tab_11")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_11)
        self.pushButton_3.setGeometry(QtCore.QRect(110, 470, 151, 71))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_11)
        self.pushButton_4.setGeometry(QtCore.QRect(390, 470, 151, 71))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label = QtWidgets.QLabel(self.tab_11)
        self.label.setGeometry(QtCore.QRect(200, 70, 131, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_11)
        self.lineEdit.setGeometry(QtCore.QRect(40, 60, 141, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_11)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 110, 171, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_11)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 160, 181, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_11)
        self.lineEdit_4.setGeometry(QtCore.QRect(40, 210, 141, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_11)
        self.lineEdit_5.setGeometry(QtCore.QRect(40, 260, 141, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab_11)
        self.lineEdit_6.setGeometry(QtCore.QRect(40, 310, 141, 31))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.tab_11)
        self.lineEdit_7.setGeometry(QtCore.QRect(390, 70, 141, 31))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.tab_11)
        self.lineEdit_8.setGeometry(QtCore.QRect(360, 130, 171, 31))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_2 = QtWidgets.QLabel(self.tab_11)
        self.label_2.setGeometry(QtCore.QRect(210, 110, 131, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab_11)
        self.label_3.setGeometry(QtCore.QRect(230, 160, 131, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab_11)
        self.label_4.setGeometry(QtCore.QRect(200, 220, 131, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab_11)
        self.label_5.setGeometry(QtCore.QRect(210, 280, 131, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab_11)
        self.label_6.setGeometry(QtCore.QRect(200, 320, 131, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab_11)
        self.label_7.setGeometry(QtCore.QRect(560, 70, 131, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab_11)
        self.label_8.setGeometry(QtCore.QRect(570, 140, 131, 16))
        self.label_8.setObjectName("label_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.tab_11)
        self.lineEdit_9.setGeometry(QtCore.QRect(340, 190, 201, 31))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_9 = QtWidgets.QLabel(self.tab_11)
        self.label_9.setGeometry(QtCore.QRect(570, 200, 131, 16))
        self.label_9.setObjectName("label_9")
        self.tabWidget_2.addTab(self.tab_11, "")
        self.tab_12 = QtWidgets.QWidget()
        self.tab_12.setObjectName("tab_12")
        self.tabWidget_2.addTab(self.tab_12, "")
        self.tabWidget.addTab(self.tab, "")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.tabWidget.addTab(self.tab_9, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        self.tabWidget_2.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Кодирование"))
        self.pushButton.setText(_translate("MainWindow", "Отправить"))
        self.pushButton_2.setText(_translate("MainWindow", "Принять"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_10), _translate("MainWindow", "Кодирование"))
        self.pushButton_3.setText(_translate("MainWindow", "Отправить"))
        self.pushButton_4.setText(_translate("MainWindow", "Принять"))
        self.label.setText(_translate("MainWindow", "Почтовый сервер"))
        self.lineEdit.setText(_translate("MainWindow", "smtp.yandex.ru"))
        self.lineEdit_2.setText(_translate("MainWindow", "mail4studying@yandex.ru"))
        self.lineEdit_3.setText(_translate("MainWindow", "endga34nogam44543421"))
        self.lineEdit_4.setText(_translate("MainWindow", "danyamelman@yandex.ru"))
        self.lineEdit_5.setText(_translate("MainWindow", "Тема сообщения"))
        self.lineEdit_6.setText(_translate("MainWindow", "Текст сообщения"))
        self.lineEdit_7.setText(_translate("MainWindow", "imap.yandex.ru"))
        self.lineEdit_8.setText(_translate("MainWindow", "danyamelman@yandex.ru"))
        self.label_2.setText(_translate("MainWindow", "Почта"))
        self.label_3.setText(_translate("MainWindow", "Пароль"))
        self.label_4.setText(_translate("MainWindow", "Получатель"))
        self.label_5.setText(_translate("MainWindow", "Тема письма"))
        self.label_6.setText(_translate("MainWindow", "Текст сообщения"))
        self.label_7.setText(_translate("MainWindow", "Сервер"))
        self.label_8.setText(_translate("MainWindow", "Логин"))
        self.lineEdit_9.setText(_translate("MainWindow", "roHB5m8kmy9sdKUm52QoAX2"))
        self.label_9.setText(_translate("MainWindow", "Пароль"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_11), _translate("MainWindow", "Отправка по почте"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_12), _translate("MainWindow", "Декодирование"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Отправка по почте"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_9), _translate("MainWindow", "Декодирование"))
