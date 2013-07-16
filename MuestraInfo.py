#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

import acerca_de
from PySide import QtGui, QtCore

from acerca_de import Ui_Form

class InfoApp(QtGui.QDialog):
	
	def __init__(self):
		super(InfoApp, self).__init__()
		self.ui = Ui_Form()
		self.ui.setupUi(self)
		
		self.show()
		self.set_listeners()
		
	def set_listeners(self):
		self.ui.pushButton.clicked.connect(self.salir)
		
	def salir(self):
		self.reject()
		
		
		
def run():
	app = QtGui.QApplication(sys.argv)
	main = InfoApp()
	sys.exit(app.exec_())
	
if __name__ == '__main__':
	run()
