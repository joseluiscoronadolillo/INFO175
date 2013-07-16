#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide import QtGui, QtCore

import controller3
from edita_cliente import Ui_Form

class Form(QtGui.QDialog):
    def __init__(self, parent=None, rut=None):
        QtGui.QDialog.__init__(self, parent)
        self.ui =  Ui_Form()
        self.ui.setupUi(self)

        if rut is None:
            self.ui.pushButton.clicked.connect(self.agregar)
        else:
			self.rut= rut
			datos_cliente = controller3.obtener_cliente(rut)
			self.ui.lineEdit.setText(datos_cliente["Rut"])
			self.ui.lineEdit_2.setText(datos_cliente["Nombres"])
			self.ui.lineEdit_3.setText(str(datos_cliente["Apellidos"]))
			self.ui.lineEdit_4.setText(str(datos_cliente["Correo"]))
			self.ui.lineEdit_5.setText(str(datos_cliente["CantidadVentas"]))
			self.ui.lineEdit_6.setText(str(datos_cliente["Total"]))
			
			self.ui.pushButton.clicked.connect(self.edita)
		
	self.ui.pushButton_2.clicked.connect(self.cancel)
  
  
  
  
	#agregar un producto a la base de datos
    def agregar(self):
		Rut= self.ui.lineEdit.text()
		Nombres = self.ui.lineEdit_2.text()
		Apellidos = self.ui.lineEdit_3.text()
		Correo = self.ui.lineEdit_4.text()
		CantidadVentas = self.ui.lineEdit_5.text()
		Total = self.ui.lineEdit_6.text()
		resultado = controller3.crear_cliente(Rut, Nombres, Apellidos,Correo, CantidadVentas, Total)
		
		if resultado:
			self.reject() #Cerramos y esto cargara nuevamente la grilla
		else:
			self.ui.errorMessageDialog = QtGui.QErrorMessage(self)
			self.ui.errorMessageDialog.showMessage("Hubo un problema al intentar crear el cliente")
						
    def cancel(self):
        self.reject()  
    
    def edita(self):
		Rut = self.ui.lineEdit.text()
		Nombres = self.ui.lineEdit_2.text()
		Apellidos = self.ui.lineEdit_3.text()
		Correo = self.ui.lineEdit_4.text()
		CantidadVentas = self.ui.lineEdit_5.text()
		Total = self.ui.lineEdit_6.text()
		resultado = controller3.editar_cliente(Rut, Nombres, Apellidos,Correo, CantidadVentas, Total)
		
		if resultado:
			self.reject()
		else:
			self.ui.errorMessageDialog = QtGui.QErrorMessage(self)
			self.ui.errorMessageDialog.showMessage("Hubo un problema al intentar editar el cliente")
