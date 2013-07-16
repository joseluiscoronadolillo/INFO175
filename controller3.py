#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import sqlite3


def connect():
    con = sqlite3.connect('ventas.db')
    con.row_factory = sqlite3.Row
    return con
    

def obtener_clientes():
    con = connect()
    c = con.cursor()
    query = """SELECT a.Rut, a.Nombres, a.Apellidos, a.Correo, a.CantidadVentas, a.Total
			FROM cliente a WHERE a.Rut"""
    resultado= c.execute(query)
    clientes = resultado.fetchall()
    con.close()
    return clientes

def obtener_cliente(rut):
	con = connect()
	c = con.cursor()
	query= "SELECT * FROM cliente WHERE Rut = ?"
	resultado = c.execute(query, [rut])
	cliente = resultado.fetchone()
	con.close
	return cliente

def buscar_cliente(word):
	con = connect()
	c = con.cursor()
	query = """SELECT a.Rut, a.Nombres, a.Apellidos, a.CantidadVentas, a.Total
			FROM cliente a WHERE a.Rut
			AND (a.Rut LIKE '%'||?||'%' )"""
	resultado = c.execute(query, [word])
	clientes = resultado.fetchall()
	con.close()
	return clientes
	
