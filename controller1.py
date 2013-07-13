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


def delete(id_sucursal):
    exito = False
    con = connect()
    c = con.cursor()
    query = "DELETE FROM sucursal WHERE Id_sucursal = ?"
    try:
        resultado = c.execute(query, [id_sucursal])
        con.commit()
        exito = True
    except sqlite3.Error as e:
        exito = False
        print "Error:", e.args[0]
    con.close()
    return exito
