# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Clientes.ui'
#
# Created: Mon Jul 15 19:55:45 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Cliente(object):
    def setupUi(self, Cliente):
        Cliente.setObjectName("Cliente")
        Cliente.resize(720, 460)
        self.Btn_search_1 = QtGui.QPushButton(Cliente)
        self.Btn_search_1.setGeometry(QtCore.QRect(460, 30, 100, 30))
        self.Btn_search_1.setObjectName("Btn_search_1")
        self.Search_box_1 = QtGui.QLineEdit(Cliente)
        self.Search_box_1.setGeometry(QtCore.QRect(160, 30, 290, 30))
        self.Search_box_1.setObjectName("Search_box_1")
        self.Eliminar_1 = QtGui.QPushButton(Cliente)
        self.Eliminar_1.setGeometry(QtCore.QRect(610, 420, 100, 30))
        self.Eliminar_1.setObjectName("Eliminar_1")
        self.Editar_1 = QtGui.QPushButton(Cliente)
        self.Editar_1.setGeometry(QtCore.QRect(510, 420, 100, 30))
        self.Editar_1.setObjectName("Editar_1")
        self.Crear_1 = QtGui.QPushButton(Cliente)
        self.Crear_1.setGeometry(QtCore.QRect(410, 420, 100, 30))
        self.Crear_1.setObjectName("Crear_1")
        self.Btn_menu = QtGui.QPushButton(Cliente)
        self.Btn_menu.setGeometry(QtCore.QRect(10, 420, 100, 30))
        self.Btn_menu.setObjectName("Btn_menu")
        self.tableView = QtGui.QTableView(Cliente)
        self.tableView.setGeometry(QtCore.QRect(10, 80, 700, 320))
        self.tableView.setObjectName("tableView")

        self.retranslateUi(Cliente)
        QtCore.QMetaObject.connectSlotsByName(Cliente)

    def retranslateUi(self, Cliente):
        Cliente.setWindowTitle(QtGui.QApplication.translate("Cliente", "Clientes", None, QtGui.QApplication.UnicodeUTF8))
        self.Btn_search_1.setText(QtGui.QApplication.translate("Cliente", "Buscar", None, QtGui.QApplication.UnicodeUTF8))
        self.Search_box_1.setPlaceholderText(QtGui.QApplication.translate("Cliente", "Buscar clientes por nombre aquí", None, QtGui.QApplication.UnicodeUTF8))
        self.Eliminar_1.setText(QtGui.QApplication.translate("Cliente", "Eliminar", None, QtGui.QApplication.UnicodeUTF8))
        self.Editar_1.setText(QtGui.QApplication.translate("Cliente", "Editar", None, QtGui.QApplication.UnicodeUTF8))
        self.Crear_1.setText(QtGui.QApplication.translate("Cliente", "Crear", None, QtGui.QApplication.UnicodeUTF8))
        self.Btn_menu.setText(QtGui.QApplication.translate("Cliente", "Menu", None, QtGui.QApplication.UnicodeUTF8))

