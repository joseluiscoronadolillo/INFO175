#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import sqlite3


def connect():
    con = sqlite3.connect('ventas.db')
    con.row_factory = sqlite3.Row
    return con
    

def obtener_sucursales():
    con = connect()
    c = con.cursor()
    query = """SELECT a.Id_sucursal, a.Ciudad, a.Direccion, a.CantidadVentas, a.Total
			FROM sucursal a WHERE a.Id_sucursal"""
    resultado= c.execute(query)
    sucursales = resultado.fetchall()
    con.close()
    return sucursales
    
def obtener_sucursal(ciudad):
	con = connect()
	c = con.cursor()
	query= "SELECT * FROM sucursal WHERE ciudad = ?"
	resultado = c.execute(query, [ciudad])
	sucursal = resultado.fetchone()
	con.close
	return sucursal
	
def buscar_sucursal(word):
	con = connect()
	c = con.cursor()
	query = """SELECT a.Id_sucursal, a.Ciudad, a.Direccion, a.CantidadVentas, a.Total
			FROM sucursal a WHERE a.Id_sucursal
			AND (a.Ciudad LIKE '%'||?||'%' )"""
	resultado = c.execute(query, [word])
	sucursales = resultado.fetchall()
	con.close()
	return sucursales

def crear_sucursal(Ciudad, Direccion, CantidadVentas, Total):
	exito = False
	con = connect()
	c = con.cursor()
	values = [Ciudad, Direccion, CantidadVentas, Total]
	query = "INSERT INTO sucursal (Ciudad, Direccion, CantidadVentas, Total) VALUES (?,?,?,?)"
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
def editar_sucursal(Ciudad, Direccion, CantidadVentas, Total):
	exito = False
	con = connect()
	c = con.cursor()
	values = [ Direccion, CantidadVentas, Total, Ciudad]
	query = """UPDATE  Sucursal SET Direccion = ?, CantidadVentas= ?, Total= ? WHERE Ciudad = ?"""
	try:
		resultado = c.execute(query, values)
		con.commit()
		exito = True
	except sqlite3.Error as e:
		exito = False
		print "Error:", e.args[0]
	con.close()
	return exito
	
def delete(ciudad):
    exito = False
    con = connect()
    c = con.cursor()
    query = "DELETE FROM sucursal WHERE ciudad = ?"
    try:
        resultado = c.execute(query, [ciudad])
        con.commit()
        exito = True
    except sqlite3.Error as e:
        exito = False
        print "Error:", e.args[0]
    con.close()
    return exito
