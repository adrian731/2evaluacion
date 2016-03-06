#!/usr/bin/env python
#-*- coding: utf-8 -*-

#3.- Pedir una edad por teclado y buscar accidentes en los que haya implicados que tengan la 
#edad introducida o menor. Mostrar la edad, el papel que ocupaba en el coche (conductor, acompañante) y el estado del afectado.
from lxml import etree

accidents=etree.parse('accidentes.xml')
raiz=accidents.getroot()
accidentes=raiz.findall("result/accidente")

teclado=int(raw_input("Introduce la edad máxima de un implicado en un accidente: "))
afectados=accidents.findall("afectado/afectado")

for a in afectados:
	if int("age") <=teclado:
		print "edad\t"+age.text,"\nrol\t"+type.text,"\nestado\t"+status.text
	else 
		print "Error"
			










#for a in accidentes:
#	if int(a.find("afectado/afectado/age").text) <= teclado:
#		print a.find("afectado/afectado/age").text +"\n"+ a.find("afectado/afectado/type").text +"\n"+a.find("afectado/afectado/status").text
#	else:
#		print "No hay accidentes con personas menores de: %s " % teclado
#		teclado=int(raw_input("Introduce otra edad máxima: "))
