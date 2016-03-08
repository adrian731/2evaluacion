#!/usr/bin/env python
#-*- coding: utf-8 -*-
import json
trabajo=open("trabajo.json","r")    
trabajos=json.load(trabajo)

teclado=raw_input("Introduce un mes(MM): ")
ofertas=[]
encontrado=False
for t in trabajos["document"]["list"]:
	for l in t["element"]["attribute"]:
		if l["name"]=="FechaModificacion":
			if teclado == l["valor"][5:7] and 		if l["name"]=="Titulo_es":
				ofertas.append(l)
				encontrado=True
if encontrado=True
print len(ofertas)
