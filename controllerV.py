#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import sqlite3


def conectar():
    con = sqlite3.connect('ventas.db')
    con.row_factory = sqlite3.Row
    return con

def crear_bd(db_name):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("""CREATE TABLE ventas("Id_venta" integer primary key AUTOINCREMENT, "Fecha" date, "Documento" text, "Detalle" text, "Neto" int, "IVA" int, "Total" int, "fk_id_sucursal" int, "fk_rut" text)""")
    c.execute("""INSERT INTO ventas VALUES(1, "09/07/2013", "Cheque", "Blusa", 10000, 1900, 11900, 1, "17585114-3")""")
    c.execute("""INSERT INTO ventas VALUES(2, "09/07/2013", "Cheque", "Blusa", 10000, 1900, 11900, 5, "16806320-2")""")
    
    c.execute("""CREATE TABLE sucursal("Id_sucursal" integer primary key AUTOINCREMENT, "Ciudad" text, "Direccion" text, "CantidadVentas" int, "Total" int)""")
    c.execute("""INSERT INTO sucursal VALUES (1,"Iquique","Héroes de la Concepción 2555", 10, 100000)""")
    c.execute("""INSERT INTO sucursal VALUES (2,"Antofagasta","Balmaceda 2355 Mall Plaza", 10, 100000)""")
    c.execute("""INSERT INTO sucursal VALUES (3,"Copiapó","O'Higgins 739", 10, 100000)""")
    c.execute("""INSERT INTO sucursal VALUES (4,"La Serena","Alberto Solari 1400 Mall Plaza", 10, 100000)""")
    c.execute("""INSERT INTO sucursal VALUES (5,"Viña del Mar","Sucre 250", 10, 100000)""")
    c.execute("""INSERT INTO sucursal VALUES (6,"Valparaíso","Independencia 1800", 10, 100000)""")
    c.execute("""INSERT INTO sucursal VALUES (7,"Providencia","Avenida Andrés Bello 2461", 10, 100000)""")
    c.execute("""INSERT INTO sucursal VALUES (8,"Las Condes","Av.Kennedy 9001 Local 1001", 10, 100000)""")
    c.execute("""INSERT INTO sucursal VALUES (9,"Las Condes","Avenida Manquehue Sur N°329", 10, 100000)""")
    c.execute("""INSERT INTO sucursal VALUES (10,"Santiago Centro","Ahumada 25", 10, 100000)""")
    c.execute("""INSERT INTO sucursal VALUES (11,"Melipilla","Vargas 457", 10, 100000)""")
    c.execute("""INSERT INTO sucursal VALUES (12, "Rancagua","Sargento Cuevas 405", 10, 100000)""") 
    c.execute("""INSERT INTO sucursal VALUES (13,"Talca","1 Norte 1485", 10, 100000)""")
    c.execute("""INSERT INTO sucursal VALUES (14,"Concepción","Barros Arana 802", 10, 100000)""")
    c.execute("""INSERT INTO sucursal VALUES (15,"Temuco","Arturo Prat 570", 10, 100000)""")
    c.execute("""INSERT INTO sucursal VALUES (16,"Valdivia","Arauco 561", 10, 100000)""")
    c.execute("""INSERT INTO sucursal VALUES (17,"Osorno","Eleuterio Ramírez 840", 10, 100000)""")
    c.execute("""INSERT INTO sucursal VALUES (18,"Puerto Montt","Av. Juan Soler Manfredini 101", 10, 100000)""")
    c.execute("""INSERT INTO sucursal VALUES (19,"Punta Arenas","Avenida Frei 01110", 10, 100000)""")
    
    c.execute("""CREATE TABLE cliente(Rut text primary key, "Nombres" text, "Apellidos" text, "Correo" text, "CantidadVentas" int, "Total" int)""")
    c.execute("""INSERT INTO cliente VALUES ("17068451-6","Soraya Maritza","Delgado Muñoz", "soraya7589@hotmail.com", 1, 10000)""")
    c.execute("""INSERT INTO cliente VALUES ("17585114-3","Ana Gabriela","Salazar Legal", "annie.gsl@outlook.com", 1, 10000)""")
    c.execute("""INSERT INTO cliente VALUES ("16806320-2","Mauricio Exzequiel","Oyarzún Gallardo", "huntermo7@gmail.com", 1, 10000)""")
    c.execute("""INSERT INTO cliente VALUES ("17693283-k","Jorge Andrés","Almonacid Aburto","coke_skate@hotmail.com", 1, 10000)""")
    c.execute("""INSERT INTO cliente VALUES ("17125455-8","José Luis","Coronado Lillo","jose_182.osorno@hotmail.com", 1, 10000)""")
    conn.commit()
    return conn

#muestra todas las ventas
def obtener_ventas():
    con = conectar()
    c = con.cursor()
    query = """SELECT a.Id_venta, a.Fecha, a.Documento, a.Detalle, a.Neto, a.IVA, a.Total, b.Ciudad as 'Sucursal'
			FROM ventas a, sucursal b WHERE a.fk_id_sucursal = b.id_sucursal"""
    resultado= c.execute(query)
    ventas = resultado.fetchall()
    con.close()
    return ventas


#muestra ventas por filtro    
def obtener_venta(id_sucursal):
    con = conectar()
    c = con.cursor()
    query = """SELECT a.Id_venta, a.Fecha, a.Documento, a.Detalle, a.Neto, a.IVA, a.Total, b.Ciudad as 'Sucursal'
			FROM ventas a, sucursal b WHERE a.fk_id_sucursal = b.id_sucursal AND a.fk_id_sucursal = ?"""
    resultado= c.execute(query, [id_sucursal])
    ventas = resultado.fetchall()
    con.close()
    return ventas


def obtener_sucursales():
	con = conectar()
	c = con.cursor()
	query = """SELECT Id_sucursal, Ciudad FROM sucursal"""
	resultado = c.execute(query)
	sucursales = resultado.fetchall()
	con.close()
	return sucursales
	


def buscar_venta(word):
	con = conectar()
	c = con.cursor()
	query = """SELECT a.Id_venta, a.Fecha, a.Documento, a.Detalle, a.Neto, a.IVA, a.Total, b.Nombres as 'Cliente'
			FROM ventas a, cliente b WHERE a.fk_rut = b.Rut
			AND (a.fk_rut LIKE '%'||?||'%' )"""
	resultado = c.execute(query, [word])
	ventas = resultado.fetchall()
	con.close()
	return ventas
	
def delete(id_venta):
    exito = False
    con = conectar()
    c = con.cursor()
    query = "DELETE FROM ventas WHERE Id_venta = ?"
    try:
        resultado = c.execute(query, [id_venta])
        con.commit()
        exito = True
    except sqlite3.Error as e:
        exito = False
        print "Error:", e.args[0]
    con.close()
    return exito

if __name__ == "__main__":
	
	db_name = 'ventas.db'
	if not os.path.exists(db_name):
		crear_bd(db_name)
