#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

from PySide import QtGui, QtCore
from Clientes import Ui_Cliente


class ProductosApp(QtGui.QWidget):

    def __init__(self):
        super(ProductosApp, self).__init__()
        self.ui =  Ui_Cliente()
        self.ui.setupUi(self)
        self.load_productos()  
        self.get_productos()  
       

		
    def load_productos(self, productos=None):
        if productos is None:
            productos = self.get_productos()

        #Creamos el modelo asociado a la tabla
        self.model = QtGui.QStandardItemModel(len(productos), 4)
        self.model.setHorizontalHeaderItem(0, QtGui.QStandardItem(u"Rut"))
        self.model.setHorizontalHeaderItem(1, QtGui.QStandardItem(u"Nombre"))
        self.model.setHorizontalHeaderItem(2, QtGui.QStandardItem(u"Apellido"))
        self.model.setHorizontalHeaderItem(3, QtGui.QStandardItem(u"Correo"))
        
        r = 0
        for row in productos:
            index = self.model.index(r, 0, QtCore.QModelIndex()); 
            self.model.setData(index, row['rut'])
            index = self.model.index(r, 1, QtCore.QModelIndex()); 
            self.model.setData(index, row['nombre'])
            index = self.model.index(r, 2, QtCore.QModelIndex()); 
            self.model.setData(index, row['apellido'])
            index = self.model.index(r, 3, QtCore.QModelIndex()); 
            self.model.setData(index, row['correo'])
            r = r+1

        self.ui.tabla_clientes.setModel(self.model)
        self.ui.tabla_clientes.setColumnWidth(0, 60)
        self.ui.tabla_clientes.setColumnWidth(1, 270)
        self.ui.tabla_clientes.setColumnWidth(2, 150)
        self.ui.tabla_clientes.setColumnWidth(3, 150)
        


def run():
    app = QtGui.QApplication(sys.argv)
    main = ProductosApp()
    sys.exit(app.exec_())

if __name__ == '__main__':
    run()
