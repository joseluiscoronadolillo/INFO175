# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ventas.ui'
#
# Created: Tue Jul 16 19:47:38 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Ventas(object):
    def setupUi(self, Ventas):
        Ventas.setObjectName("Ventas")
        Ventas.resize(730, 470)
        self.FiltroSucursales = QtGui.QComboBox(Ventas)
        self.FiltroSucursales.setGeometry(QtCore.QRect(100, 30, 241, 31))
        self.FiltroSucursales.setToolTip("")
        self.FiltroSucursales.setWhatsThis("")
        self.FiltroSucursales.setAutoFillBackground(False)
        self.FiltroSucursales.setObjectName("FiltroSucursales")
        self.CrearVenta = QtGui.QPushButton(Ventas)
        self.CrearVenta.setGeometry(QtCore.QRect(420, 430, 100, 30))
        self.CrearVenta.setObjectName("CrearVenta")
        self.EditarVenta = QtGui.QPushButton(Ventas)
        self.EditarVenta.setGeometry(QtCore.QRect(520, 430, 100, 30))
        self.EditarVenta.setObjectName("EditarVenta")
        self.TablaVentas = QtGui.QTableView(Ventas)
        self.TablaVentas.setGeometry(QtCore.QRect(10, 90, 710, 320))
        self.TablaVentas.setObjectName("TablaVentas")
        self.EliminarVenta = QtGui.QPushButton(Ventas)
        self.EliminarVenta.setGeometry(QtCore.QRect(620, 430, 100, 31))
        self.EliminarVenta.setObjectName("EliminarVenta")
        self.BackToMenu = QtGui.QPushButton(Ventas)
        self.BackToMenu.setGeometry(QtCore.QRect(10, 430, 100, 30))
        self.BackToMenu.setObjectName("BackToMenu")
        self.Busqueda = QtGui.QLineEdit(Ventas)
        self.Busqueda.setGeometry(QtCore.QRect(400, 30, 221, 31))
        self.Busqueda.setInputMask("")
        self.Busqueda.setText("")
        self.Busqueda.setObjectName("Busqueda")
        self.BuscarLabel = QtGui.QPushButton(Ventas)
        self.BuscarLabel.setGeometry(QtCore.QRect(620, 30, 100, 30))
        self.BuscarLabel.setObjectName("BuscarLabel")
        self.label = QtGui.QLabel(Ventas)
        self.label.setGeometry(QtCore.QRect(20, 35, 60, 21))
        self.label.setObjectName("label")

        self.retranslateUi(Ventas)
        QtCore.QMetaObject.connectSlotsByName(Ventas)

    def retranslateUi(self, Ventas):
        Ventas.setWindowTitle(QtGui.QApplication.translate("Ventas", "Ventas", None, QtGui.QApplication.UnicodeUTF8))
        self.CrearVenta.setText(QtGui.QApplication.translate("Ventas", "Crear", None, QtGui.QApplication.UnicodeUTF8))
        self.EditarVenta.setText(QtGui.QApplication.translate("Ventas", "Editar", None, QtGui.QApplication.UnicodeUTF8))
        self.EliminarVenta.setText(QtGui.QApplication.translate("Ventas", "Eliminar", None, QtGui.QApplication.UnicodeUTF8))
        self.BackToMenu.setText(QtGui.QApplication.translate("Ventas", "Menu", None, QtGui.QApplication.UnicodeUTF8))
        self.Busqueda.setPlaceholderText(QtGui.QApplication.translate("Ventas", "Ingrese lo que desea buscar", None, QtGui.QApplication.UnicodeUTF8))
        self.BuscarLabel.setText(QtGui.QApplication.translate("Ventas", "Buscar", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Ventas", " Sucursal", None, QtGui.QApplication.UnicodeUTF8))

