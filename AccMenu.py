#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

import Venta
import Sucursal
import Cliente 
import MuestraInfo
from PySide import QtGui, QtCore
from MenuPrincipal import Ui_MenuPrincipal

class MenuApp(QtGui.QDialog):
	
	def __init__(self):
		super(MenuApp, self).__init__()
		self.ui = Ui_MenuPrincipal()
		self.ui.setupUi(self)

		self.show()
		self.set_listeners()
	

	def set_listeners(self):
		self.ui.IrSucursal.clicked.connect(self.show_sucursal)
		self.ui.IrCliente.clicked.connect(self.show_cliente)
		self.ui.IrVenta.clicked.connect(self.show_venta)
		self.ui.Salir.clicked.connect(self.cerrar_ventana)
		self.ui.Info.clicked.connect(self.mostrar_datos)
		
	def show_sucursal(self):
		self.reject()
		form = Sucursal.SucursalApp()
		form.exec_()
		
	def show_cliente(self):
		self.reject()
		form = Cliente.ClientesApp()
		form.exec_()
		
	def show_venta(self):
		self.reject()
		form = Venta.VentasApp()
		form.exec_()
		
	def cerrar_ventana(self):
		self.reject()
		
	def mostrar_datos(self):
		form = MuestraInfo.InfoApp()
		form.exec_()
			


def run():
	app = QtGui.QApplication(sys.argv)
	main = MenuApp()
	sys.exit(app.exec_())
	
if __name__ == '__main__':
	run()

