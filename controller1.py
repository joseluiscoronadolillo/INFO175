#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3


def connect():
    con = sqlite3.connect('marcas.db')
    con.row_factory = sqlite3.Row
    return con

def get_productos():
    con = connect()
    c = con.cursor()
    query = """SELECT a.rut, a.nombres, a.apellidos, a.correo, b.nombre as 'marca'
            FROM productos a, marcas b WHERE a.fk_id_marca = b.id_marca"""
    result = c.execute(query)
    productos = result.fetchall()
    con.close()
    return productos
