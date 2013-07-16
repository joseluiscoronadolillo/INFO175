#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

from PySide import QtGui, QtCore
from Clientes import Ui_Cliente
import controller3
import Clientes
import MenuPrincipal
import AccMenu

from Sucursales import Ui_Sucursal
from edita_sucursal import Ui_Form

class ClienteApp(QtGui.QWidget):

    def __init__(self):
        super(ClienteApp, self).__init__()
        self.ui =  Ui_Cliente()
        self.ui.setupUi(self)
        self.cargar_clientes() 
        self.show 
        self.set_listeners()
        
		
    def cargar_clientes(self, cliente=None):
        if cliente is None:
            cliente = controller3.obtener_clientes()

        #Creamos el modelo asociado a la tabla
        self.model = QtGui.QStandardItemModel(len(cliente), 6)
        self.model.setHorizontalHeaderItem(0, QtGui.QStandardItem(u"Rut"))
        self.model.setHorizontalHeaderItem(1, QtGui.QStandardItem(u"Nombre"))
        self.model.setHorizontalHeaderItem(2, QtGui.QStandardItem(u"Apellido"))
        self.model.setHorizontalHeaderItem(3, QtGui.QStandardItem(u"Correo"))
        self.model.setHorizontalHeaderItem(4, QtGui.QStandardItem(u"CantidadVentas"))
        self.model.setHorizontalHeaderItem(5, QtGui.QStandardItem(u"Total"))
        
        r = 0
        for row in cliente:
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
            self.model.setData(index, row['Total'])
            r = r+1

        self.ui.tabla_clientes.setModel(self.model)
        self.ui.tabla_clientes.setColumnWidth(0, 60)
        self.ui.tabla_clientes.setColumnWidth(1, 270)
        self.ui.tabla_clientes.setColumnWidth(2, 150)
        self.ui.tabla_clientes.setColumnWidth(3, 150)
        self.ui.tabla_clientes.setColumnWidth(4, 150)
        self.ui.tabla_clientes.setColumnWidth(5, 150)
        
    def volver(self):
		self.reject()
		form = AccMenu.MenuApp()
		form.exec_()    


def run():
    app = QtGui.QApplication(sys.argv)
    main = ClienteApp()
    sys.exit(app.exec_())

if __name__ == '__main__':
    run()
