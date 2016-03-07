#!/usr/bin/env python
#-*- coding: utf-8 -*-
import json
trabajo=open("trabajo.json","r")    
trabajos=json.load(trabajo)

teclado=raw_input("Introduce una fecha(YYYY-MM-DD): ")

for t in trabajos["document"]["list"]:
	for l in t["element"]["attribute"]:
		if l["name"]=="FechaModificacion":
			if l["valor"].split(" ")[0] == teclado:
				if "Enlace al contenido" == l["name"]: 
					print l["valor"]
