#!/usr/bin/env python
#-*- coding: utf-8 -*-

from lxml import etree

accidents=etree.parse('accidentes.xml')
raiz=accidents.getroot()
accidentes=raiz.findall("result/accidente")

teclado=int(raw_input("Introduce la edad máxima de un implicado en un accidente: "
for a in accidentes:
	
	if int(a.find("afectado/afectado/age").text) <= teclado:
		print a.find("afectado/afectado/age").text +"\n"+ a.find("afectado/afectado/type").text +"\n"+a.find("afectado/afectado/status").text
		
	else:
		print "No hay accidentes con personas menores de: " +teclado+
		teclado=int(raw_input("Introduce otra edad máxima: "
		
	
		
	
