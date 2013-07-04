#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys

from PySide import QtGui, QtCore
#import controller
import Ventas
import MenuPrincipal
import AccMenu

from Ventas import Ui_Ventas

class VentasApp(QtGui.QDialog):
	
	def __init__(self):
		super(VentasApp, self).__init__()
		self.ui = Ui_Ventas()
		self.ui.setupUi(self)
		self.cargar_ventas()
		#self.cargar_marcas()

		self.show()
		self.set_listeners()
	

	def set_listeners(self):
		self.ui.FiltroSucursales.activated[int].connect(self.cargar_sucursales)
		#self.ui.producto.activated[int].connect(self.completar)
		self.ui.BuscarLabel.clicked.connect(self.cargar_venta_por_buscar)
		self.ui.CrearVenta.clicked.connect(self.show_add)
		self.ui.EditarVenta.clicked.connect(self.show_edit)
		self.ui.EliminarVenta.clicked.connect(self.delete)
		self.ui.BackToMenu.clicked.connect(self.volver)
		#self.ui.table_productos.doubleClicked.connect(self.show_edit)
		


#	def cargar_marcas(self):
		#marcas = controller.obtener_marcas()
		#self.ui.combo_marcas.addItem("Todos",-1)
		#for marca in marcas:
		#	self.ui.combo_marcas.addItem(marca["nombre"], marca["id_marca"])
		#self.ui.combo_marcas.setEditable(True)
		#completer = QtGui.QCompleter(map(lambda c: c["nombre"], marcas), self)
		#completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
		#self.ui.combo_marcas.setCompleter(completer)
		
#MODIFICAR DEPENDIENDO DEL CONTROLLER
	def cargar_venta_por_buscar(self):
		word = self.ui.busqueda.text()
		#ventas = controller. Metodo (word)
		#self.cargar_ventas(ventas)
		

	def cargar_sucursales(self, index):
		print "Cargar sucursales"
		#id_marca = self.ui.combo_marcas.itemData(self.ui.combo_marcas.currentIndex())
		#if id_marca == -1:
			#productos = controller.obtener_productos()
		#else:
			#productos = controller.obtener_producto(id_marca)
		#self.cargar_productos(productos)
	

	def cargar_ventas(self, ventas = None):
		if ventas is None:
			print "Ventas de la tabla"
			#ventas = controller.obtener_productos()
		
		#self.model = QtGui.QStandardItemModel(len(ventas),8)
		#self.model.setHorizontalHeaderItem(0, QtGui.QStandardItem(u"Fecha"))
		#self.model.setHorizontalHeaderItem(1, QtGui.QStandardItem(u"Documento"))
		#self.model.setHorizontalHeaderItem(2, QtGui.QStandardItem(u"Sucursal"))
		#self.model.setHorizontalHeaderItem(3, QtGui.QStandardItem(u"Rut"))
		#self.model.setHorizontalHeaderItem(4, QtGui.QStandardItem(u"Detalle"))
		#self.model.setHorizontalHeaderItem(5, QtGui.QStandardItem(u"Neto"))
		#self.model.setHorizontalHeaderItem(6, QtGui.QStandardItem(u"IVA"))
		#self.model.setHorizontalHeaderItem(7, QtGui.QStandardItem(u"Total"))
		#r = 0
		#for row in productos:
		#	index = self.model.index(r, 0, QtCore.QModelIndex());
		#	self.model.setData(index, row[''])
		#	index = self.model.index(r, 1, QtCore.QModelIndex());
		#	self.model.setData(index, row[''])
		#	index = self.model.index(r, 2, QtCore.QModelIndex());
		#	self.model.setData(index, row[''])
		#	index = self.model.index(r, 3, QtCore.QModelIndex());
		#	self.model.setData(index, row[''])
		#	index = self.model.index(r, 4, QtCore.QModelIndex());
		#	self.model.setData(index, row[''])
		#	index = self.model.index(r, 5, QtCore.QModelIndex());
		#	self.model.setData(index, row[''])
		#	index = self.model.index(r, 6, QtCore.QModelIndex());
		#	self.model.setData(index, row[''])
		#	index = self.model.index(r, 7, QtCore.QModelIndex());
		#	self.model.setData(index, row[''])
		#	r = r+1
		
		#self.ui.TablaVentas.setModel(self.model)
		#self.ui.TablaVentas.setColumnWidth(0,50)
		#self.ui.TablaVentas.setColumnWidth(1,50)
		#self.ui.TablaVentas.setColumnWidth(2,100)
		#self.ui.TablaVentas.setColumnWidth(3,100)
		#self.ui.TablaVentas.setColumnWidth(4,100)
		#self.ui.TablaVentas.setColumnWidth(5,100)
		#self.ui.TablaVentas.setColumnWidth(6,100)
		#self.ui.TablaVentas.setColumnWidth(7,100)
	
	
	def show_add(self):
		print "Abre ventana para agregar"
		

	def show_edit(self):
		model = self.ui.TablaVentas.model()
		index = self.ui.TablaVentas.currentIndex()
		if index.row() == -1:
			self.errorMessageDialog = QtGui.QErrorMessage(self)
			self.errorMessageDialog.showMessage(" Debe seleccionar una fila")
			return False
		else:
			print "Abre ventana para editar"
			#codigo = model.index(index.row(), 0, QtCore.QModelIndex()).data()
			#form = agrega_view.Form(self, codigo)
			#form.rejected.connect(self.cargar_productos)
			#form.exec_()
	
		
	def delete(self):
		model = self.ui.TablaVentas.model()
		index = self.ui.TablaVentas.currentIndex()
		if index.row() == -1:
			self.errorMessageDialog = QtGui.QErrorMessage(self)
			self.errorMessageDialog.showMessage(" Debe seleccionar una fila")
			return False
		else:
			print " eliminando fila"
			#codigo = model.index(index.row(), 0, QtCore.QModelIndex()).data()
			#self.cargar_productos()
			#msgBox = QtGui.QMessageBox()
			#msgBox.setText("El registro fue eliminado.")
			#msgBox.setInformativeText("Desea guardar los cambios?")
			#msgBox.setStandardButtons(QtGui.QMessageBox.Save | QtGui.QMessageBox.Discard | QtGui.QMessageBox.Cancel)
			#msgBox.setDefaultButton(QtGui.QMessageBox.Save)
			#ret = msgBox.exec_()
			#if ret == QtGui.QMessageBox.Save:
				#controller.delete(codigo)
				#self.cargar_productos()
				#return True
			#else:
			#	self.ui.errorMessageDialog = QtGui.QErrorMessage(self)
			#	self.ui.errorMessageDialog.showMessage(" El registro no fue eliminado")
			#	return False
		self.ui.FiltroSucursales.addItem("Todos",-1)
		
	def volver(self):
		self.reject()
		form = AccMenu.MenuApp()
		form.exec_()
		


def run():
	app = QtGui.QApplication(sys.argv)
	main = VentasApp()
	sys.exit(app.exec_())
	
if __name__ == '__main__':
	run()
