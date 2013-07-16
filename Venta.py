#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys

from PySide import QtGui, QtCore
import controller2
import controller1
import MenuPrincipal
import AccMenu
import agrga_ven

from Ventas import Ui_Ventas

class VentasApp(QtGui.QDialog):
	
	def __init__(self):
		super(VentasApp, self).__init__()
		self.ui = Ui_Ventas()
		self.ui.setupUi(self)
		self.cargar_ventas()
		self.cargar_sucursal()

		self.show()
		self.set_listeners()
	

	def set_listeners(self):
		self.ui.FiltroSucursales.activated[int].connect(self.cargar_sucursales)
		self.ui.BuscarLabel.clicked.connect(self.cargar_venta_por_buscar)
		self.ui.CrearVenta.clicked.connect(self.show_add)
		self.ui.EditarVenta.clicked.connect(self.show_edit)
		self.ui.EliminarVenta.clicked.connect(self.delete)
		self.ui.BackToMenu.clicked.connect(self.volver)
		self.ui.TablaVentas.doubleClicked.connect(self.show_edit)
		


	def cargar_sucursal(self):
		sucursales = controller1.obtener_sucursales()
		self.ui.FiltroSucursales.addItem("Todos",-1)
		for sucursal in sucursales:
			self.ui.FiltroSucursales.addItem(sucursal["Ciudad"], sucursal["Id_sucursal"])
		self.ui.FiltroSucursales.setEditable(True)
		completer = QtGui.QCompleter(map(lambda c: c["Ciudad"], sucursales), self)
		completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
		self.ui.FiltroSucursales.setCompleter(completer)
		

	def cargar_venta_por_buscar(self):
		word = self.ui.Busqueda.text()
		ventas = controller2.buscar_venta(word)
		self.cargar_ventas(ventas)
		

	def cargar_sucursales(self, index):
		id_sucursal = self.ui.FiltroSucursales.itemData(self.ui.FiltroSucursales.currentIndex())
		if id_sucursal == -1:
			ventas = controller2.obtener_ventas()
		else:
			ventas = controller2.obtener_venta(id_sucursal)
		self.cargar_ventas(ventas)
	

	def cargar_ventas(self, ventas = None):
		if ventas is None:
			ventas = controller2.obtener_ventas()
		
		self.model = QtGui.QStandardItemModel(len(ventas),6)
		self.model.setHorizontalHeaderItem(0, QtGui.QStandardItem(u"Fecha"))
		self.model.setHorizontalHeaderItem(1, QtGui.QStandardItem(u"Tipo Documento"))
		self.model.setHorizontalHeaderItem(2, QtGui.QStandardItem(u"Detalle Compra"))
		self.model.setHorizontalHeaderItem(3, QtGui.QStandardItem(u"Neto"))
		self.model.setHorizontalHeaderItem(4, QtGui.QStandardItem(u"IVA"))
		self.model.setHorizontalHeaderItem(5, QtGui.QStandardItem(u"Total"))
		r = 0
		for row in ventas:
			index = self.model.index(r, 0, QtCore.QModelIndex());
			self.model.setData(index, row['Fecha'])
			index = self.model.index(r, 1, QtCore.QModelIndex());
			self.model.setData(index, row['Documento'])
			index = self.model.index(r, 2, QtCore.QModelIndex());
			self.model.setData(index, row['Detalle'])
			index = self.model.index(r, 3, QtCore.QModelIndex());
			self.model.setData(index, row['Neto'])
			index = self.model.index(r, 4, QtCore.QModelIndex());
			self.model.setData(index, row['IVA'])
			index = self.model.index(r, 5, QtCore.QModelIndex());
			self.model.setData(index, row['Total'])
			r = r+1
		
		self.ui.TablaVentas.setModel(self.model)
		self.ui.TablaVentas.setColumnWidth(0,100)
		self.ui.TablaVentas.setColumnWidth(1,100)
		self.ui.TablaVentas.setColumnWidth(2,150)
		self.ui.TablaVentas.setColumnWidth(3,150)
		self.ui.TablaVentas.setColumnWidth(4,100)
		self.ui.TablaVentas.setColumnWidth(5,100)
	
	#Falta implementar
	def show_add(self):
		#print "Abre ventana para agregar"
		edita_venta = agrga_ven.Form(self)
		edita_venta.rejected.connect(self.cargar_ventas)
		edita_venta.exec_()
		

	#Falta implementar
	def show_edit(self):
		model = self.ui.TablaVentas.model()
		index = self.ui.TablaVentas.currentIndex()
		if index.row() == -1:
			self.errorMessageDialog = QtGui.QErrorMessage(self)
			self.errorMessageDialog.showMessage(" Debe seleccionar una fila")
			return False
		else:
			print "Abre ventana para editar"
			fecha = model.index(index.row(), 0, QtCore.QModelIndex()).data()
			form = agrga_ven.Form(self, fecha)
			form.rejected.connect(self.cargar_ventas)
			form.exec_()
	
	
	#NO FUNCIONA	
	def delete(self):
		model = self.ui.TablaVentas.model()
		index = self.ui.TablaVentas.currentIndex()
		if index.row() == -1:
			self.errorMessageDialog = QtGui.QErrorMessage(self)
			self.errorMessageDialog.showMessage(" Debe seleccionar una fila")
			return False
		else:
			id_venta = model.index(index.row(), 0, QtCore.QModelIndex()).data()
			self.cargar_ventas()
			msgBox = QtGui.QMessageBox()
			msgBox.setText("El registro fue eliminado.")
			msgBox.setInformativeText("Seguro que desea eliminar?")
			msgBox.setStandardButtons(QtGui.QMessageBox.Save | QtGui.QMessageBox.Discard | QtGui.QMessageBox.Cancel)
			msgBox.setDefaultButton(QtGui.QMessageBox.Save)
			ret = msgBox.exec_()
			if ret == QtGui.QMessageBox.Save:
				controller2.delete(id_venta)
				self.cargar_ventas()
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
	main = VentasApp()
	sys.exit(app.exec_())
	
if __name__ == '__main__':
	run()
