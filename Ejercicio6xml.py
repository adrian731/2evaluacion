#!/usr/bin/env python
#-*- coding: utf-8 -*-
from lxml import etree


#Programa que pida un año y genere un fichero html con la siguiente información:
#<h1>Tipo accidente</h1>
#<p>Razon del accidente</p>
#<ul>
#	<li>Edad afectado- Estado</li>
#	<li>Edad afectado- Estado</li>
#	<li>...
#</ul>
accidents=etree.parse('accidentes.xml')
raiz=accidents.getroot()
accidentes=raiz.findall("result/accidente")


teclado=raw_input("Introduce el año(YYYY): ")
fechas=raiz.findall("result/accidente/creationDate")
encontrado=False

fich=open("index.html","w")

for f,a in zip(fechas,accidentes):
	edad=a.find("afectado/afectado/age")
	estado=a.find("afectado/afectado/status")
	tipo=("result/accidente/type")
	razon=("result/accidente/reason")
	if f.text[0:4]==teclado:
		encontrado=True
		try:
			fich.write("<html></br><head></head></br><body><h1>"+a.find("afectado/afectado/age")+"</h1></br><p>"+a.find("afectado/afectado/status"+"</br>)</p>")
			fich.write("<ul>"+"\n"+"<li>"+a.find("afectado/afectado/age").text+"\t-\t"+a.find("afectado/afectado/status").text+"</li>"+"</ul>")
			fich.write("</br></body></br></html>") 
		except:
			pass


fich.close()