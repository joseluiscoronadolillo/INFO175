#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide import QtGui, QtCore

import controller2
import controller1
import controller3
from edita_venta import Ui_nueva_venta

class Form(QtGui.QDialog):
    def __init__(self, parent=None, Id_venta=None):
		QtGui.QDialog.__init__(self, parent)
		self.ui =  Ui_nueva_venta()
		self.ui.setupUi(self)
		self.cargar_ven()
		self.cargar_cli()
		
		if Id_venta is None:
			self.ui.Aceptar.clicked.connect(self.agregar)
		else:
			self.Id_venta = Id_venta
			datos_venta = controller2.obtener_venta(Id_venta)
			self.ui.editafecha.setText(str(datos_venta["Fecha"]))
			self.ui.lineEdit.setText(str(datos_venta["Documentos"]))
			self.ui.lineEdit_3.setText(str(datos_venta["Detalle"]))
			self.ui.lineEdit_2.setText(str(datos_venta["Neto"]))

			self.ui.Aceptar.clicked.connect(self.edita)
		self.ui.pushButton.clicked.connect(self.cancel)
  
	#agregar un producto a la base de datos
    def agregar(self):
		
		Fecha = self.ui.editafecha.text()
		Documentos = self.ui.lineEdit.text()
		Detalle = self.ui.lineEdit_3.text()
		Neto = self.ui.lineEdit_2.text()
		neto2 = int(Neto)
		netofloat = float(neto2)
		Iva = netofloat * 0.19
		Total = netofloat + Iva
		fk_ciudad = self.ui.comboBox.itemData(self.ui.comboBox.currentIndex())
		fk_rut = self.ui.comboBox_2.itemData(self.ui.comboBox_2.currentIndex())
		resultado = controller2.crear_venta(Fecha, Documentos, Detalle, Neto, Iva, Total, fk_ciudad, fk_rut)
		
		if resultado:
			self.reject() #Cerramos y esto cargara nuevamente la grilla
		else:
			self.ui.errorMessageDialog = QtGui.QErrorMessage(self)
			self.ui.errorMessageDialog.showMessage("Hubo un problema al intentar crear la venta")
			
						
    def cancel(self):
        self.reject()
        
        
    def cargar_ven(self):
		sucursales = controller1.obtener_sucursales()
		for sucursal in sucursales:
			self.ui.comboBox.addItem(sucursal["ciudad"], sucursal["Id_sucursal"])
	
    def cargar_cli(self):
		clientes = controller3.obtener_clientes()
		for cliente in clientes:
			self.ui.comboBox_2.addItem(cliente["rut"], cliente["Rut"])
    
    def edita(self):
		Fecha = self.ui.editafecha.text()
		Documentos = self.ui.lineEdit.text()
		Detalle = self.ui.lineEdit_3.text()
		Neto = self.ui.lineEdit_2.text()
		fk_ciudad = self.ui.comboBox.itemData(self.ui.comboBox.currentIndex())
		fk_rut = self.ui.comboBox_2.itemData(self.ui.comboBox_2.currentIndex())
		resultado = controller2.editar_venta(Fecha, Documentos, Detalle, Neto, fk_ciudad, fk_rut)
		print "editando cliente"
		
		if resultado:
			self.reject()
			
		else:
			self.ui.errorMessageDialog = QtGui.QErrorMessage(self)
			self.ui.errorMessageDialog.showMessage("Hubo un problema al intentar editar la venta")
