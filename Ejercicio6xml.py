#!/usr/bin/env python
#-*- coding: utf-8 -*-

#Programa que pida un año y genere un fichero html con la siguiente información:
#<h1>Tipo accidente</h1>
#<p>Razon del accidente</p>
#<ul>
#	<li>Edad afectado- Estado</li>
#	<li>Edad afectado- Estado</li>
#	<li>...
#</ul>

from lxml import etree
accidents=etree.parse('accidentes.xml')
raiz=accidents.getroot()
accidentes=raiz.findall("result/accidente")


teclado=raw_input("Introduce el año(YYYY): ")
fechas=raiz.findall("result/accidente/creationDate")
tipo=("result/accidente/type")
razon=("result/accidente/reason")
encontrado=False

for f,a in zip(fechas,accidentes):
	edad=a.find("afectado/afectado/age")
	estado=a.find("afectado/afectado/status")
	if f.text[0:4]==teclado:
		encontrado=True
		try:
			print a.find("afectado/afectado/age").text+"\t-\t"+a.find("afectado/afectado/status").text
		except:
			pass
			


with open("accidentes.html", "w") as fi:
  fi.write("<html></head><body>")
  fi.write("<h1>%</h1></br><p>%<p>" % (tipo,razon))
  fi.write("<ul><li>%\t-\t</li></ul>")

