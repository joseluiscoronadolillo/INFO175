#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

from PySide import QtGui, QtCore
import controller3
import MenuPrincipal
import AccMenu
import agrega_cli

from Clientes import Ui_Cliente
from edita_cliente import Ui_Form

class ClientesApp(QtGui.QDialog):
	def __init__(self):
		super(ClientesApp, self).__init__()
		self.ui = Ui_Cliente()
		self.ui.setupUi(self)
		self.cargar_clientes()
		self.show()
		self.set_listeners()
		
	def set_listeners(self):
		self.ui.Btn_search_1.clicked.connect(self.buscar_clientes)
		self.ui.Btn_menu.clicked.connect(self.volver)
		self.ui.Crear_1.clicked.connect(self.show_add)
		self.ui.Editar_1.clicked.connect(self.show_edit)
		self.ui.Eliminar_1.clicked.connect(self.delete)
		
		
	def buscar_clientes(self):
		word = self.ui.Search_box_1.text()
		clientes = controller3.buscar_cliente(word)
		self.cargar_clientes(clientes)
			
	def show_add(self):
		print "Abre ventana para agregar"
		edita_sucursal = agrega_suc.Form(self)
		edita_sucursal.rejected.connect(self.cargar_sucursales)
		edita_sucursal.exec_()
		
	def cargar_clientes(self, clientes=None):
		if clientes is None:
			clientes = controller3.obtener_clientes()
		
		self.model = QtGui.QStandardItemModel(len(clientes), 6)
		self.model.setHorizontalHeaderItem(0, QtGui.QStandardItem(u"Rut"))
		self.model.setHorizontalHeaderItem(1, QtGui.QStandardItem(u"Nombres"))
		self.model.setHorizontalHeaderItem(2, QtGui.QStandardItem(u"Apellidos"))
		self.model.setHorizontalHeaderItem(3, QtGui.QStandardItem(u"Correo"))
		self.model.setHorizontalHeaderItem(4, QtGui.QStandardItem(u"CantidadVentas"))
		self.model.setHorizontalHeaderItem(5, QtGui.QStandardItem(u"Total"))
		r = 0
		for row in clientes:
			index = self.model.index(r, 0, QtCore.QModelIndex()); 
			self.model.setData(index, row['Rut'])
			index = self.model.index(r, 1, QtCore.QModelIndex()); 
			self.model.setData(index, row['Nombres'])
			index = self.model.index(r, 2, QtCore.QModelIndex()); 
			self.model.setData(index, row['Apellidos'])
			index = self.model.index(r, 3, QtCore.QModelIndex()); 
			self.model.setData(index, row['Correo'])
			index = self.model.index(r, 4, QtCore.QModelIndex()); 
			self.model.setData(index, row['CantidadVentas'])
			index = self.model.index(r, 5, QtCore.QModelIndex()); 
			self.model.setData(index, row['total'])
			r = r+1
		self.ui.tableView.setModel(self.model)
		self.ui.tableView.setColumnWidth(0, 150)
		self.ui.tableView.setColumnWidth(1, 270)
		self.ui.tableView.setColumnWidth(2, 150)
		self.ui.tableView.setColumnWidth(3, 150)
		self.ui.tableView.setColumnWidth(4, 150)
		self.ui.tableView.setColumnWidth(5, 150)
		
	def show_add(self):
		print "Abre ventana para agregar"
		edita_cliente = agrega_cli.Form(self)
		edita_cliente.rejected.connect(self.cargar_clientes)
		edita_cliente.exec_()
		
	def show_edit(self):
		model = self.ui.tableView.model()
		index = self.ui.tableView.currentIndex()
		if index.row() == -1:
			self.errorMessageDialog = QtGui.QErrorMessage(self)
			self.errorMessageDialog.showMessage(" Debe seleccionar una fila")
			return False
		else:
			#print "Abre ventana para editar"
			Rut = model.index(index.row(), 0, QtCore.QModelIndex()).data()
			edita_cliente = agrega_cli.Form(self,Rut)
			edita_cliente.rejected.connect(self.cargar_clientes)
			edita_cliente.exec_()
			
	def delete(self):
		model = self.ui.tableView.model()
		index = self.ui.tableView.currentIndex()
		if index.row() == -1:
			self.errorMessageDialog = QtGui.QErrorMessage(self)
			self.errorMessageDialog.showMessage(" Debe seleccionar una fila")
			return False
		else:
			Rut = model.index(index.row(), 0, QtCore.QModelIndex()).data()
			self.cargar_clientes()
			msgBox = QtGui.QMessageBox()
			msgBox.setText("El registro fue eliminado.")
			msgBox.setInformativeText("Desea guardar los cambios?")
			msgBox.setStandardButtons(QtGui.QMessageBox.Save | QtGui.QMessageBox.Discard | QtGui.QMessageBox.Cancel)
			msgBox.setDefaultButton(QtGui.QMessageBox.Save)
			ret = msgBox.exec_()
			if ret == QtGui.QMessageBox.Save:
				controller3.delete(Rut)
				self.cargar_clientes()
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
    main = ClientesApp()
    sys.exit(app.exec_())

if __name__ == '__main__':
    run()
