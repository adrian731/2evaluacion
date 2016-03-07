#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Busca todos los accidentes que se hayan producido a causa de un fallo mecánico o los que no. (campo falloMecánico).
#Muestra la razón y en qué estado estaban el pavimento y la atmósfera.
from lxml import etree

accidents=etree.parse('accidentes.xml')
raiz=accidents.getroot()
accidentes=raiz.findall("result/accidente")

teclado=raw_input( "Estamos tratando sobre accidentes. ¿Quiere buscar los que se han producido por un fallo mecánico o los que no?\nsi/no: ")
for a in accidentes:
	if teclado == a.find("falloMecanico"):
		print a.find("vehiculo/vehiculo/quantity").text +" Vehículo/s implicados." 
		print "Pavimento: "+ a.find("estadoPavimento").text
		print "Atmófera: "+ a.find("estadoAtmosfera").text +"\n"
	else:	
		print "Error"
