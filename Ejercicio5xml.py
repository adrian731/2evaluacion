#!/usr/bin/env python
#-*- coding: utf-8 -*-

#Introduce una fecha (YYYY-MM-DD) y haz un programa que te muestre qué accidentes se han dado en esa fecha, la dirección y las coordenadas del mismo.

from lxml import etree
accidents=etree.parse('accidentes.xml')
raiz=accidents.getroot()
accidentes=raiz.findall("result/accidente")


teclado=raw_input("Introduce la fecha(YYYY-MM-DD): ")
fechas=raiz.findall("result/accidente/creationDate")
for f,a in zip(fechas,accidentes):
	if f.text[0:10]== teclado:
		print a.find("firstAddress").text+"\n"+a.find("secondAddress").text+"\n"+a.find("geometry/coordinates").text
	else:

		print "La fecha no es válida o no se encuentra en la base de datos"
