#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

from PySide import QtGui, QtCore
import controller1
import Sucursales
import MenuPrincipal
import AccMenu
import agrega_suc

from Sucursales import Ui_Sucursal
from edita_sucursal import Ui_Form

class SucursalApp(QtGui.QDialog):
	
	def __init__(self):
		super(SucursalApp, self).__init__()
		self.ui = Ui_Sucursal()
		self.ui.setupUi(self)
		self.cargar_sucursales()
		self.show()
		self.set_listeners()
		
	def set_listeners(self):
		self.ui.Btn_search.clicked.connect(self.buscar_sucursales)
		self.ui.Crear.clicked.connect(self.show_add)
		self.ui.Editar.clicked.connect(self.show_edit)
		self.ui.Eliminar.clicked.connect(self.delete)
		self.ui.Btn_menu_1.clicked.connect(self.volver)
		
	def buscar_sucursales(self):
		word = self.ui.Search_box.text()
		sucursales = controller1.buscar_sucursal(word)
		self.cargar_sucursales(sucursales)
		
		
	def cargar_sucursales(self, sucursales = None):
		if sucursales is None:
			sucursales = controller1.obtener_sucursales()
		
		self.model = QtGui.QStandardItemModel(len(sucursales),4)
		self.model.setHorizontalHeaderItem(0, QtGui.QStandardItem(u"Ciudad"))
		self.model.setHorizontalHeaderItem(1, QtGui.QStandardItem(u"Dirección"))
		self.model.setHorizontalHeaderItem(2, QtGui.QStandardItem(u"Cantidad de Ventas"))
		self.model.setHorizontalHeaderItem(3, QtGui.QStandardItem(u"Total en Ventas"))
		r = 0
		for row in sucursales:
			index = self.model.index(r, 0, QtCore.QModelIndex());
			self.model.setData(index, row['Ciudad'])
			index = self.model.index(r, 1, QtCore.QModelIndex());
			self.model.setData(index, row['Direccion'])
			index = self.model.index(r, 2, QtCore.QModelIndex());
			self.model.setData(index, row['CantidadVentas'])
			index = self.model.index(r, 3, QtCore.QModelIndex());
			self.model.setData(index, row['Total'])
			r = r+1
		
		self.ui.tableView.setModel(self.model)
		self.ui.tableView.setColumnWidth(0,150)
		self.ui.tableView.setColumnWidth(1,300)
		self.ui.tableView.setColumnWidth(2,150)
		self.ui.tableView.setColumnWidth(3,150)
		
			
	def show_add(self):
		print "Abre ventana para agregar"
		edita_sucursal = agrega_suc.Form(self)
		edita_sucursal.rejected.connect(self.cargar_sucursales)
		edita_sucursal.exec_()
			
	def show_edit(self):
		model = self.ui.tableView.model()
		index = self.ui.tableView.currentIndex()
		if index.row() == -1:
			self.errorMessageDialog = QtGui.QErrorMessage(self)
			self.errorMessageDialog.showMessage(" Debe seleccionar una fila")
			return False
			
		else:
			
			ciudad = model.index(index.row(), 0, QtCore.QModelIndex()).data()
			Form= agrega_suc.Form(self,ciudad)
			Form.rejected.connect(self.cargar_sucursales)
			Form.exec_()
			
			
	          
	def delete(self):
		model = self.ui.tableView.model()
		index = self.ui.tableView.currentIndex()
		if index.row() == -1:
			self.errorMessageDialog = QtGui.QErrorMessage(self)
			self.errorMessageDialog.showMessage(" Debe seleccionar una fila")
			return False
		else:
			id_sucursal = model.index(index.row(), 0, QtCore.QModelIndex()).data()
			self.cargar_sucursales()
			msgBox = QtGui.QMessageBox()
			msgBox.setText("El registro fue eliminado.")
			msgBox.setInformativeText("Desea guardar los cambios?")
			msgBox.setStandardButtons(QtGui.QMessageBox.Save | QtGui.QMessageBox.Discard | QtGui.QMessageBox.Cancel)
			msgBox.setDefaultButton(QtGui.QMessageBox.Save)
			ret = msgBox.exec_()
			if ret == QtGui.QMessageBox.Save:
				controller1.delete(id_sucursal)
				self.cargar_sucursales()
				return True
			else:
				self.ui.errorMessageDialog = QtGui.QErrorMessage(self)
				self.ui.errorMessageDialog.showMessage(" El registro no fue eliminado")
				return False
		self.ui.FiltroSucursales.addItem("Todos",-1)
		
	def volver(self):
		self.reject()
		form = AccMenu.MenuApp()
		form.exec_()
		
		
def run():
	app = QtGui.QApplication(sys.argv)
	main = SucursalApp()
	sys.exit(app.exec_())
	
if __name__ == '__main__':
	run()
