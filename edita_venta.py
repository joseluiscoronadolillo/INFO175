# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edita_venta.ui'
#
# Created: Tue Jul 16 00:54:50 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_nueva_venta(object):
    def setupUi(self, nueva_venta):
        nueva_venta.setObjectName("nueva_venta")
        nueva_venta.resize(443, 298)
        self.Aceptar = QtGui.QPushButton(nueva_venta)
        self.Aceptar.setGeometry(QtCore.QRect(180, 250, 98, 27))
        self.Aceptar.setObjectName("Aceptar")
        self.editafecha = QtGui.QLineEdit(nueva_venta)
        self.editafecha.setGeometry(QtCore.QRect(110, 20, 111, 21))
        self.editafecha.setObjectName("editafecha")
        self.label = QtGui.QLabel(nueva_venta)
        self.label.setGeometry(QtCore.QRect(20, 20, 51, 21))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(nueva_venta)
        self.label_2.setGeometry(QtCore.QRect(18, 50, 91, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(nueva_venta)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 51, 21))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtGui.QLineEdit(nueva_venta)
        self.lineEdit.setGeometry(QtCore.QRect(110, 50, 311, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtGui.QLineEdit(nueva_venta)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 110, 161, 21))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_5 = QtGui.QLabel(nueva_venta)
        self.label_5.setGeometry(QtCore.QRect(20, 80, 66, 17))
        self.label_5.setObjectName("label_5")
        self.lineEdit_3 = QtGui.QLineEdit(nueva_venta)
        self.lineEdit_3.setGeometry(QtCore.QRect(110, 80, 191, 21))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_7 = QtGui.QLabel(nueva_venta)
        self.label_7.setGeometry(QtCore.QRect(20, 140, 211, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtGui.QLabel(nueva_venta)
        self.label_8.setGeometry(QtCore.QRect(20, 180, 201, 16))
        self.label_8.setObjectName("label_8")
        self.comboBox = QtGui.QComboBox(nueva_venta)
        self.comboBox.setGeometry(QtCore.QRect(240, 140, 78, 27))
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtGui.QComboBox(nueva_venta)
        self.comboBox_2.setGeometry(QtCore.QRect(240, 180, 78, 27))
        self.comboBox_2.setObjectName("comboBox_2")
        self.pushButton = QtGui.QPushButton(nueva_venta)
        self.pushButton.setGeometry(QtCore.QRect(310, 250, 98, 27))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(nueva_venta)
        QtCore.QMetaObject.connectSlotsByName(nueva_venta)

    def retranslateUi(self, nueva_venta):
        nueva_venta.setWindowTitle(QtGui.QApplication.translate("nueva_venta", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.Aceptar.setText(QtGui.QApplication.translate("nueva_venta", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.editafecha.setPlaceholderText(QtGui.QApplication.translate("nueva_venta", "ej: 11/07/2013", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("nueva_venta", "Fecha:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("nueva_venta", " Documento:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("nueva_venta", "Neto:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit.setPlaceholderText(QtGui.QApplication.translate("nueva_venta", "ej: cheque, factura,efectivo, crédito o débito ", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_2.setPlaceholderText(QtGui.QApplication.translate("nueva_venta", "ej:10000, sin puntos", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("nueva_venta", "Detalle:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_3.setPlaceholderText(QtGui.QApplication.translate("nueva_venta", "ej: blusa, lo que se compró", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("nueva_venta", "Asocie la venta a una sucursal:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("nueva_venta", "Asocie la venta a un cliente:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("nueva_venta", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

