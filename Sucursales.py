# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Sucursales.ui'
#
# Created: Thu Jun 27 11:17:12 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Sucursal(object):
    def setupUi(self, Sucursal):
        Sucursal.setObjectName("Sucursal")
        Sucursal.resize(720, 460)
        self.Eliminar = QtGui.QPushButton(Sucursal)
        self.Eliminar.setGeometry(QtCore.QRect(610, 420, 100, 30))
        self.Eliminar.setObjectName("Eliminar")
        self.Editar = QtGui.QPushButton(Sucursal)
        self.Editar.setGeometry(QtCore.QRect(510, 420, 100, 30))
        self.Editar.setObjectName("Editar")
        self.Crear = QtGui.QPushButton(Sucursal)
        self.Crear.setGeometry(QtCore.QRect(410, 420, 100, 30))
        self.Crear.setObjectName("Crear")
        self.Tabla_sucursales = QtGui.QListView(Sucursal)
        self.Tabla_sucursales.setGeometry(QtCore.QRect(10, 80, 700, 320))
        self.Tabla_sucursales.setObjectName("Tabla_sucursales")
        self.Btn_search = QtGui.QPushButton(Sucursal)
        self.Btn_search.setGeometry(QtCore.QRect(460, 30, 100, 30))
        self.Btn_search.setObjectName("Btn_search")
        self.Search_box = QtGui.QLineEdit(Sucursal)
        self.Search_box.setGeometry(QtCore.QRect(160, 30, 290, 30))
        self.Search_box.setStyleSheet("")
        self.Search_box.setObjectName("Search_box")
        self.Btn_menu_1 = QtGui.QPushButton(Sucursal)
        self.Btn_menu_1.setGeometry(QtCore.QRect(10, 420, 98, 27))
        self.Btn_menu_1.setObjectName("Btn_menu_1")

        self.retranslateUi(Sucursal)
        QtCore.QMetaObject.connectSlotsByName(Sucursal)

    def retranslateUi(self, Sucursal):
        Sucursal.setWindowTitle(QtGui.QApplication.translate("Sucursal", "Sucursales", None, QtGui.QApplication.UnicodeUTF8))
        self.Eliminar.setText(QtGui.QApplication.translate("Sucursal", "Eliminar", None, QtGui.QApplication.UnicodeUTF8))
        self.Editar.setText(QtGui.QApplication.translate("Sucursal", "Editar", None, QtGui.QApplication.UnicodeUTF8))
        self.Crear.setText(QtGui.QApplication.translate("Sucursal", "Crear", None, QtGui.QApplication.UnicodeUTF8))
        self.Btn_search.setText(QtGui.QApplication.translate("Sucursal", "Buscar", None, QtGui.QApplication.UnicodeUTF8))
        self.Search_box.setPlaceholderText(QtGui.QApplication.translate("Sucursal", "Buscar sucursal aquí", None, QtGui.QApplication.UnicodeUTF8))
        self.Btn_menu_1.setText(QtGui.QApplication.translate("Sucursal", "Menu", None, QtGui.QApplication.UnicodeUTF8))

