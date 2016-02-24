#!/usr/bin/env python
#-*- coding: utf-8 -*-

from lxml import etree

accidents=etree.parse('accidentes.xml')
raiz=accidents.getroot()
accidentes=raiz.findall("result/accidente")

teclado=raw_input("Introduce la ID de un accidente: ")
for a in accidentes:
	if teclado == a.find("id").text:
		tipos=a.findall("vehiculo/vehiculo/type")
		for t in tipos:
			print t.text
		

