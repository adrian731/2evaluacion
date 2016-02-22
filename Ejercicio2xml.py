#!/usr/bin/env python
#-*- coding: utf-8 -*-

from lxml import etree

accidents=etree.parse('accidentes.xml')
raiz=accidents.getroot()
accidentes=raiz.findall("result/accidente")


teclado=raw_input( "Estamos tratando sobre accidentes. ¿Quiere buscar los que se han producido por un fallo mecánico o los que no?\nsí/no: ")
for a in accidentes:
	if upper.teclado == a.find("falloMecanico").text:
		print a.find("vehiculo/quantity").text
		print "Pavimento: "+ a.find("estadoPavimento").text
		print "Atmófera: "+ a.find("estadoAtmosfera").text
