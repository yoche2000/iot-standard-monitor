# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\OneNET-MQ-Demo-Python-20190830\OneNET-MQ-Demo-Python\client.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_client(object):
    def setupUi(self, client):
        client.setObjectName("client")
        client.resize(758, 341)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(client.sizePolicy().hasHeightForWidth())
        client.setSizePolicy(sizePolicy)
        client.setMinimumSize(QtCore.QSize(758, 341))
        client.setMaximumSize(QtCore.QSize(758, 341))
        self.label_temp_symbol = QtWidgets.QLabel(client)
        self.label_temp_symbol.setGeometry(QtCore.QRect(150, 90, 121, 91))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.label_temp_symbol.setFont(font)
        self.label_temp_symbol.setAlignment(QtCore.Qt.AlignCenter)
        self.label_temp_symbol.setObjectName("label_temp_symbol")
        self.label_humidity_value = QtWidgets.QLabel(client)
        self.label_humidity_value.setGeometry(QtCore.QRect(320, 90, 121, 91))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.label_humidity_value.setFont(font)
        self.label_humidity_value.setAlignment(QtCore.Qt.AlignCenter)
        self.label_humidity_value.setObjectName("label_humidity_value")
        self.label_humidity_title = QtWidgets.QLabel(client)
        self.label_humidity_title.setGeometry(QtCore.QRect(320, 40, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.label_humidity_title.setFont(font)
        self.label_humidity_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_humidity_title.setObjectName("label_humidity_title")
        self.label_1451 = QtWidgets.QLabel(client)
        self.label_1451.setGeometry(QtCore.QRect(580, 70, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_1451.setFont(font)
        self.label_1451.setMouseTracking(True)
        self.label_1451.setTextFormat(QtCore.Qt.RichText)
        self.label_1451.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_1451.setObjectName("label_1451")
        self.label_humidity_accuracy = QtWidgets.QLabel(client)
        self.label_humidity_accuracy.setGeometry(QtCore.QRect(320, 180, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_humidity_accuracy.setFont(font)
        self.label_humidity_accuracy.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.label_humidity_accuracy.setAlignment(QtCore.Qt.AlignCenter)
        self.label_humidity_accuracy.setObjectName("label_humidity_accuracy")
        self.label_2668 = QtWidgets.QLabel(client)
        self.label_2668.setGeometry(QtCore.QRect(580, 120, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2668.setFont(font)
        self.label_2668.setMouseTracking(True)
        self.label_2668.setTextFormat(QtCore.Qt.RichText)
        self.label_2668.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2668.setObjectName("label_2668")
        self.label_humidity_symbol = QtWidgets.QLabel(client)
        self.label_humidity_symbol.setGeometry(QtCore.QRect(440, 90, 121, 91))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.label_humidity_symbol.setFont(font)
        self.label_humidity_symbol.setAlignment(QtCore.Qt.AlignCenter)
        self.label_humidity_symbol.setObjectName("label_humidity_symbol")
        self.label_temp_accuracy = QtWidgets.QLabel(client)
        self.label_temp_accuracy.setGeometry(QtCore.QRect(30, 180, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_temp_accuracy.setFont(font)
        self.label_temp_accuracy.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.label_temp_accuracy.setAlignment(QtCore.Qt.AlignCenter)
        self.label_temp_accuracy.setObjectName("label_temp_accuracy")
        self.label_temp_title = QtWidgets.QLabel(client)
        self.label_temp_title.setGeometry(QtCore.QRect(30, 40, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.label_temp_title.setFont(font)
        self.label_temp_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_temp_title.setObjectName("label_temp_title")
        self.label_temp_value = QtWidgets.QLabel(client)
        self.label_temp_value.setGeometry(QtCore.QRect(30, 90, 121, 91))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.label_temp_value.setFont(font)
        self.label_temp_value.setAlignment(QtCore.Qt.AlignCenter)
        self.label_temp_value.setObjectName("label_temp_value")
        self.label_txt = QtWidgets.QLabel(client)
        self.label_txt.setGeometry(QtCore.QRect(180, 240, 451, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_txt.setFont(font)
        self.label_txt.setObjectName("label_txt")
        self.label_idex_title = QtWidgets.QLabel(client)
        self.label_idex_title.setGeometry(QtCore.QRect(600, 170, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_idex_title.setFont(font)
        self.label_idex_title.setMouseTracking(True)
        self.label_idex_title.setTextFormat(QtCore.Qt.RichText)
        self.label_idex_title.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_idex_title.setObjectName("label_idex_title")
        self.label_idex_value = QtWidgets.QLabel(client)
        self.label_idex_value.setGeometry(QtCore.QRect(680, 170, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_idex_value.setFont(font)
        self.label_idex_value.setMouseTracking(True)
        self.label_idex_value.setTextFormat(QtCore.Qt.RichText)
        self.label_idex_value.setAlignment(QtCore.Qt.AlignCenter)
        self.label_idex_value.setObjectName("label_idex_value")
        self.alarm = QtWidgets.QLabel(client)
        self.alarm.setGeometry(QtCore.QRect(630, 220, 91, 91))
        self.alarm.setText("")
        self.alarm.setTextFormat(QtCore.Qt.RichText)
        self.alarm.setPixmap(QtGui.QPixmap(":/newPrefix/alarm (1).png"))
        self.alarm.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.alarm.setObjectName("alarm")

        self.retranslateUi(client)
        QtCore.QMetaObject.connectSlotsByName(client)

    def retranslateUi(self, client):
        _translate = QtCore.QCoreApplication.translate
        client.setWindowTitle(_translate("client", "Client"))
        self.label_temp_symbol.setText(_translate("client", "℃"))
        self.label_humidity_value.setText(_translate("client", "--"))
        self.label_humidity_title.setText(_translate("client", "Humidity"))
        self.label_1451.setText(_translate("client", " ▋ IEEE 1451: ✓"))
        self.label_humidity_accuracy.setText(_translate("client", "Accuracy: 00%"))
        self.label_2668.setText(_translate("client", " ▋ IEEE 2668: ✓"))
        self.label_humidity_symbol.setText(_translate("client", "％"))
        self.label_temp_accuracy.setText(_translate("client", "Accuracy: 00%"))
        self.label_temp_title.setText(_translate("client", "Temperature"))
        self.label_temp_value.setText(_translate("client", "--"))
        self.label_txt.setText(_translate("client", "IEEE P2668 Standard Certified Data"))
        self.label_idex_title.setText(_translate("client", "IDex = "))
        self.label_idex_value.setText(_translate("client", "5"))
import rc2_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    client = QtWidgets.QWidget()
    ui = Ui_client()
    ui.setupUi(client)
    client.show()
    sys.exit(app.exec_())
