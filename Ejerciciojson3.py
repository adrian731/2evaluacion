#!/usr/bin/env python
#-*- coding: utf-8 -*-
import json
trabajo=open("trabajo.json","r")    
trabajos=json.load(trabajo)

teclado=raw_input("Introduce una cadena a buscar: ")

for t in trabajos["document"]["list"]:
	for l in t["element"]["attribute"]:
		if l["name"]=="Titulo_es":
			if l["text"].count(teclado)>=1:
				print l["text"]
			
