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
    c.execute("""INSERT INTO ventas VALUES(3, "10/07/2013", "Efectivo", "Pantalon", 7990, 1518, 9508, 9, "17693283-k")""")
    c.execute("""INSERT INTO ventas VALUES(4, "03/09/2012", "Crédito", "WM Lunar Forever Zapatillas Mujer", 27990, 5318, 33308, 17, "17068451-6")""")
    c.execute("""INSERT INTO ventas VALUES(5, "11/07/2013", "Efectivo", "Jeans Efesis", 20000, 3800, 23800, 1, "17585114-3")""")
    c.execute("""INSERT INTO ventas VALUES(6, "12/07/2013", "Débito", "Polera Sybilla", 23000, 4370, 27370, 1, "17585114-3")""")
    c.execute("""INSERT INTO ventas VALUES(7, "13/07/2013", "Efectivo", "Zapatillas Converse", 20000, 3800, 23800, 1, "17585114-3")""")
    c.execute("""INSERT INTO ventas VALUES(8, "14/07/2013", "Crédito", "Zapatillas All Stars", 30000, 5700, 35700, 1, "17585114-3")""")
    c.execute("""INSERT INTO ventas VALUES(9, "15/07/2013", "Crédito", "Pantalon Cotele Ellus", 23000, 4370, 27370, 1, "17585114-3")""")
    c.execute("""INSERT INTO ventas VALUES(10, "16/07/2013", "Efectivo", "Jeans Lewis", 24000, 4560, 28560, 1, "17585114-3")""")
    c.execute("""INSERT INTO ventas VALUES(11, "08/07/2013", "Débito", "Zapatillas Nike", 26000, 4940, 30940, 1, "17585114-3")""")
    c.execute("""INSERT INTO ventas VALUES(12, "07/07/2013", "Débito", "Blusa Sybilla", 23000, 4370, 27370, 1, "17585114-3")""")
    c.execute("""INSERT INTO ventas VALUES(13, "06/07/2013", "Cheque", "Jeans Lee", 22000, 4180, 26180, 1, "17585114-3")""")
    c.execute("""INSERT INTO ventas VALUES(14, "05/07/2013", "Cheque", "Jeans Fioriucci", 27000, 5130, 32130, 1, "17585114-3")""")
    
    
    c.execute("""CREATE TABLE sucursal("Id_sucursal" integer primary key AUTOINCREMENT, "Ciudad" text, "Direccion" text, "CantidadVentas" int, "Total" int)""")
    c.execute("""INSERT INTO sucursal VALUES (1,"Iquique","Héroes de la Concepción 2555", 10, 100000)""")
    c.execute("""INSERT INTO sucursal VALUES (2,"Antofagasta","Balmaceda 2355 Mall Plaza", 10, 100000)""")
    c.execute("""INSERT INTO sucursal VALUES (3,"Copiapó","O'Higgins 739", 10, 100000)""")
    c.execute("""INSERT INTO sucursal VALUES (4,"La Serena","Alberto Solari 1400 Mall Plaza", 10, 100000)""")
    c.execute("""INSERT INTO sucursal VALUES (5,"Viña del Mar","Sucre 250", 10, 100000)""")
    c.execute("""INSERT INTO sucursal VALUES (6,"Valparaíso","Independencia 1800", 10, 100000)""")
    c.execute("""INSERT INTO sucursal VALUES (7,"Providencia","Avenida Andrés Bello 2461", 10, 100000)""")
    c.execute("""INSERT INTO sucursal VALUES (8,"Las Condes","Avenida Manquehue Sur N°329", 10, 100000)""")
    c.execute("""INSERT INTO sucursal VALUES (9,"Santiago Centro","Ahumada 25", 10, 100000)""")
    c.execute("""INSERT INTO sucursal VALUES (10,"Melipilla","Vargas 457", 10, 100000)""")
    c.execute("""INSERT INTO sucursal VALUES (11, "Rancagua","Sargento Cuevas 405", 10, 100000)""") 
    c.execute("""INSERT INTO sucursal VALUES (12,"Talca","1 Norte 1485", 10, 100000)""")
    c.execute("""INSERT INTO sucursal VALUES (13,"Concepción","Barros Arana 802", 10, 100000)""")
    c.execute("""INSERT INTO sucursal VALUES (14,"Temuco","Arturo Prat 570", 10, 100000)""")
    c.execute("""INSERT INTO sucursal VALUES (15,"Valdivia","Arauco 561", 10, 100000)""")
    c.execute("""INSERT INTO sucursal VALUES (16,"Osorno","Eleuterio Ramírez 840", 10, 100000)""")
    c.execute("""INSERT INTO sucursal VALUES (17,"Puerto Montt","Av. Juan Soler Manfredini 101", 10, 100000)""")
    c.execute("""INSERT INTO sucursal VALUES (18,"Punta Arenas","Avenida Frei 01110", 10, 100000)""")
    
    c.execute("""CREATE TABLE cliente(Rut text primary key, "Nombres" text, "Apellidos" text, "Correo" text, "CantidadVentas" int, "Total" int)""")
    c.execute("""INSERT INTO cliente VALUES ("17068451-6","Soraya Maritza","Delgado Muñoz", "soraya7589@hotmail.com", 1, 10000)""")
    c.execute("""INSERT INTO cliente VALUES ("17585114-3","Ana Gabriela","Salazar Legal", "annie.gsl@outlook.com", 1, 10000)""")
    c.execute("""INSERT INTO cliente VALUES ("16806320-2","Mauricio Exzequiel","Oyarzún Gallardo", "huntermo7@gmail.com", 1, 10000)""")
    c.execute("""INSERT INTO cliente VALUES ("17693283-k","Jorge Andrés","Almonacid Aburto","coke_skate@hotmail.com", 1, 10000)""")
    c.execute("""INSERT INTO cliente VALUES ("17125455-8","José Luis","Coronado Lillo","jose_182.osorno@hotmail.com", 1, 10000)""")
    conn.commit()
    return conn



if __name__ == "__main__":
	
	db_name = 'ventas.db'
	if not os.path.exists(db_name):
		crear_bd(db_name)
