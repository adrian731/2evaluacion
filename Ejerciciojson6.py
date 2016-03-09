#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Programa que genere un fichero html con la siguiente información de las ofertas de trabajo.

#<h1>titulo</h1>
#<p>Descripción</p>
#a href="Enlace al contenido"> Más información</a>
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import json

trabajo=open("trabajo.json","r")    
trabajos=json.load(trabajo)

fich=open("index.html","w")
fich.write("<html></br><head></head></br><body>")

for t in trabajos["document"]["list"]:
	for l in t["element"]["attribute"]:
		if l["name"]=="Titulo_es":
			fich.write("<h1>"+l["text"]+"</h1></br>")
		if l["name"]=="Descripcion_es":
			fich.write("<p>"+l["text"]+"</p></br>")
		if l["name"]=="Enlace al contenido":
			fich.write("<a href=Enlace al contenido>"+l["valor"]+"</a>")

fich.write("</br></body></br></html>")

fich.close()