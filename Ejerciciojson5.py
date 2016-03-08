#!/usr/bin/env python
#-*- coding: utf-8 -*-
import json
trabajo=open("trabajo.json","r")    
trabajos=json.load(trabajo)

teclado=raw_input("Introduce un mes(MM): ")
encontrado=False
contador=0
for t in trabajos["document"]["list"]:
	for l in t["element"]["attribute"]:
		if l["name"]=="FechaModificacion":
			if teclado == l["valor"][5:7]:
				encontrado=True
				contador=contador + 1


print contador