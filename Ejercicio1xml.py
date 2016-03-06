#!/usr/bin/env python
#-*- coding: utf-8 -*-

#Buscar el tipo, la razón y las coordenadas de todos los accidentes.
from lxml import etree

accidents=etree.parse('accidentes.xml')
raiz=accidents.getroot()
accidentes=raiz.findall("result/accidente")


for a in accidentes:	
	print a.find("type").text +"\n"+ a.find("reason").text +"\n"+ a.find("geometry/coordinates").text+"\n\n"
