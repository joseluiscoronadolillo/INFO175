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
    
def obtener_cliente(Rut):
	con = connect()
	c = con.cursor()
	query= "SELECT * FROM cliente WHERE Rut = ?"
	resultado = c.execute(query, [Rut])
	cliente = resultado.fetchone()
	con.close
	return cliente
	
def buscar_cliente(word):
	con = connect()
	c = con.cursor()
	query = """SELECT a.Rut, a.Nombres, a.Apellidos, a.Correo, a.CantidadVentas, a.Total
			FROM cliente a WHERE a.Rut
			AND (a.Rut LIKE '%'||?||'%' OR a.Nombres LIKE '%'||?||'%' OR a.Apellidos LIKE '%'||?||'%' OR a.Correo LIKE '%'||?||'%' OR a.CantidadVentas LIKE '%'||?||'%' OR a.Total LIKE '%'||?||'%'  )"""
	resultado = c.execute(query, [word, word, word, word, word, word])
	clientes = resultado.fetchall()
	con.close()
	return clientes 

def crear_cliente( Rut, Nombres, Apellidos, Correo, CantidadVentas, Total):
	exito = False
	con = connect()
	c = con.cursor()
	values = [Rut, Nombres, Apellidos, Correo, CantidadVentas, Total]
	query = "INSERT INTO cliente (Rut, Nombres, Apellidos, Correo, CantidadVentas, Total) VALUES (?,?,?,?,?,?)"
	try:
		resultado = c.execute(query, values)
		con.commit()
		exito = True
	except sqlite3.Error as e:
		exito = False
		print "Error:", e.args[0]
		con.close()
	return exito
		

#Metodo que edita una fila de la tabla productos segun, direccionandose por su codigo   
def editar_cliente(Rut, Nombres, Apellidos, Correo, CantidadVentas, Total):
	exito = False
	con = connect()
	c = con.cursor()
	values = [Nombres, Apellidos, Correo, CantidadVentas, Total, Rut]
	query = """UPDATE  cliente SET Nombres = ?, Apellidos = ?, Correo = ?, CantidadVentas= ?, Total= ? WHERE Rut = ?"""
	try:
		resultado = c.execute(query, values)
		con.commit()
		exito = True
	except sqlite3.Error as e:
		exito = False
		print "Error:", e.args[0]
	con.close()
	return exito
	
def delete(Rut):
    exito = False
    con = connect()
    c = con.cursor()
    query = "DELETE FROM cliente WHERE Rut = ?"
    try:
        resultado = c.execute(query, [Rut])
        con.commit()
        exito = True
    except sqlite3.Error as e:
        exito = False
        print "Error:", e.args[0]
    con.close()
    return exito
