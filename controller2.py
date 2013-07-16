#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import sqlite3


def connect():
    con = sqlite3.connect('ventas.db')
    con.row_factory = sqlite3.Row
    return con
    
#muestra todas las ventas
def obtener_ventas():
    con = connect()
    c = con.cursor()
    query = """SELECT a.Id_venta, a.Fecha, a.Documento, a.Detalle, a.Neto, a.IVA, a.Total, b.Ciudad as 'Sucursal'
			FROM ventas a, sucursal b WHERE a.fk_id_sucursal = b.Id_sucursal"""
    resultado= c.execute(query)
    ventas = resultado.fetchall()
    con.close()
    return ventas


#muestra ventas por filtro    
def obtener_venta(Fecha):
    con = connect()
    c = con.cursor()
    query = """SELECT  a.Id_venta, a.Fecha, a.Documento, a.Detalle, a.Neto, a.IVA, a.Total, b.Ciudad as 'Sucursal'
			FROM ventas a, sucursal b WHERE a.fk_id_sucursal = b.Id_sucursal AND a.fk_id_sucursal = ?"""
    resultado= c.execute(query, [Fecha])
    ventas = resultado.fetchall()
    con.close()
    return ventas	

def buscar_venta(word):
	con = connect()
	c = con.cursor()
	query = """SELECT a.Id_venta, a.Fecha, a.Documento, a.Detalle, a.Neto, a.IVA, a.Total, b.Nombres as 'Cliente'
			FROM ventas a, cliente b WHERE a.fk_rut = b.Rut
			AND (a.fk_rut LIKE '%'||?||'%' )"""
	resultado = c.execute(query, [word])
	ventas = resultado.fetchall()
	con.close()
	return ventas
	
def delete(Id_venta):
    exito = False
    con = connect()
    c = con.cursor()
    query = "DELETE FROM ventas WHERE Id_venta = ?"
    try:
        resultado = c.execute(query, [Id_venta])
        con.commit()
        exito = True
    except sqlite3.Error as e:
        exito = False
        print "Error:", e.args[0]
    con.close()
    return exito

def crear_venta( Fecha, Documento, detalle, neto, iva, total, fk_id_sucursal, fk_rut):
	exito = False
	con = connect()
	c = con.cursor()
	values = [Fecha, Documento, detalle, neto, iva, total, fk_id_sucursal, fk_rut]
	query = """INSERT INTO ventas ( Fecha, Documento, Detalle, Neto, IVA, Total,  fk_id_sucursal, fk_rut) VALUES (?,?,?,?,?,?,?,?)"""
	try:
		resultado = c.execute(query, values)
		con.commit()
		exito = True
	except sqlite3.Error as e:
		exito = False
		print "Error:", e.args[0]
		con.close()
	return exito

def editar_venta(Fecha, Documento, detalle, neto, fk_id_sucursal, fk_rut):
	exito = False
	conn = connect()
	c = conn.cursor()
	values = [Documento, detalle, neto, fk_id_sucursal, fk_rut, Fecha]
	query = """UPDATE ventas SET Documento = ?, detalle = ?,neto =?,fk_id_sucursal = ?, fk_rut=? WHERE Fecha =?"""
	try:
		resultado = c.execute(query,values)
		conn.commit()
		exito = True
	except sqlite3.Error as e:
		exito = False
		print "Error:", e.args[0]
		conn.close()
	return exito
	
	
	
	
