# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MenuPrincipal.ui'
#
# Created: Thu Jun 27 11:28:18 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MenuPrincipal(object):
    def setupUi(self, MenuPrincipal):
        MenuPrincipal.setObjectName("MenuPrincipal")
        MenuPrincipal.resize(360, 360)
        self.label = QtGui.QLabel(MenuPrincipal)
        self.label.setGeometry(QtCore.QRect(40, 30, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        font.setPointSize(12)
        font.setWeight(75)
        font.setItalic(False)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.IrSucursal = QtGui.QPushButton(MenuPrincipal)
        self.IrSucursal.setGeometry(QtCore.QRect(130, 90, 100, 30))
        font = QtGui.QFont()
        font.setFamily("KacstLetter")
        font.setWeight(75)
        font.setBold(True)
        self.IrSucursal.setFont(font)
        self.IrSucursal.setObjectName("IrSucursal")
        self.IrCliente = QtGui.QPushButton(MenuPrincipal)
        self.IrCliente.setGeometry(QtCore.QRect(130, 140, 100, 30))
        font = QtGui.QFont()
        font.setFamily("KacstLetter")
        font.setWeight(75)
        font.setBold(True)
        self.IrCliente.setFont(font)
        self.IrCliente.setObjectName("IrCliente")
        self.IrVenta = QtGui.QPushButton(MenuPrincipal)
        self.IrVenta.setGeometry(QtCore.QRect(130, 200, 100, 30))
        font = QtGui.QFont()
        font.setFamily("KacstLetter")
        font.setWeight(75)
        font.setBold(True)
        self.IrVenta.setFont(font)
        self.IrVenta.setObjectName("IrVenta")
        self.Salir = QtGui.QPushButton(MenuPrincipal)
        self.Salir.setGeometry(QtCore.QRect(240, 310, 100, 30))
        font = QtGui.QFont()
        font.setFamily("KacstLetter")
        font.setWeight(75)
        font.setBold(True)
        self.Salir.setFont(font)
        self.Salir.setObjectName("Salir")
        self.Info = QtGui.QPushButton(MenuPrincipal)
        self.Info.setGeometry(QtCore.QRect(20, 310, 100, 30))
        font = QtGui.QFont()
        font.setFamily("KacstLetter")
        font.setWeight(75)
        font.setBold(True)
        self.Info.setFont(font)
        self.Info.setObjectName("Info")

        self.retranslateUi(MenuPrincipal)
        QtCore.QMetaObject.connectSlotsByName(MenuPrincipal)

    def retranslateUi(self, MenuPrincipal):
        MenuPrincipal.setWindowTitle(QtGui.QApplication.translate("MenuPrincipal", "Menu Principal", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MenuPrincipal", "Seleccione la opcion que desea analizar", None, QtGui.QApplication.UnicodeUTF8))
        self.IrSucursal.setText(QtGui.QApplication.translate("MenuPrincipal", "Sucursales", None, QtGui.QApplication.UnicodeUTF8))
        self.IrCliente.setText(QtGui.QApplication.translate("MenuPrincipal", "Clientes", None, QtGui.QApplication.UnicodeUTF8))
        self.IrVenta.setText(QtGui.QApplication.translate("MenuPrincipal", "Ventas", None, QtGui.QApplication.UnicodeUTF8))
        self.Salir.setText(QtGui.QApplication.translate("MenuPrincipal", "Salir", None, QtGui.QApplication.UnicodeUTF8))
        self.Info.setText(QtGui.QApplication.translate("MenuPrincipal", "Info", None, QtGui.QApplication.UnicodeUTF8))

