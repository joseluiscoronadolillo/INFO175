#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide import QtGui, QtCore

import controller1
from edita_sucursal import Ui_Form

class Form(QtGui.QDialog):
    def __init__(self, parent=None, ciudad=None):
        QtGui.QDialog.__init__(self, parent)
        self.ui =  Ui_Form()
        self.ui.setupUi(self)

        if ciudad is None:
            self.ui.pushButton.clicked.connect(self.agregar)
        else:
			self.ciudad= ciudad
			datos_sucursal = controller1.obtener_sucursal(ciudad)
			self.ui.lineEdit.setText(datos_sucursal["Ciudad"])
			self.ui.lineEdit_2.setText(datos_sucursal["Direccion"])
			self.ui.lineEdit_3.setText(str(datos_sucursal["CantidadVentas"]))
			self.ui.lineEdit_4.setText(str(datos_sucursal["Total"]))
			
			self.ui.pushButton.clicked.connect(self.edita)
		
	self.ui.pushButton_2.clicked.connect(self.cancel)
  
  
  
  
	#agregar un producto a la base de datos
    def agregar(self):
		ciudad = self.ui.lineEdit.text()
		direccion = self.ui.lineEdit_2.text()
		cantidadventa = self.ui.lineEdit_3.text()
		total = self.ui.lineEdit_4.text()
		resultado = controller1.crear_sucursal(ciudad, direccion, cantidadventa, total)
		
		if resultado:
			self.reject() #Cerramos y esto cargara nuevamente la grilla
		else:
			self.ui.mensajes.setText("Hubo un problema al intentar crear el alumno")  
						
    def cancel(self):
        self.reject()  
    
    def edita(self):
		Ciudad = self.ui.lineEdit.text()
		Direccion = self.ui.lineEdit_2.text()
		CantidadVentas = self.ui.lineEdit_3.text()
		Total = self.ui.lineEdit_4.text()
		resultado = controller1.editar_sucursal(Ciudad, Direccion, CantidadVentas, Total)
		
		if resultado:
			self.reject()
		else:
			self.ui.errorMessageDialog = QtGui.QErrorMessage(self)
			self.ui.errorMessageDialog.showMessage("Hubo un problema al intentar editar el producto")
