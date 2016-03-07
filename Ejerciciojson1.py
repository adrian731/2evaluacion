#!/usr/bin/env python
#-*- coding: utf-8 -*-
import json
trabajo=open("trabajo.json","r")    
trabajos=json.load(trabajo)


for t in trabajos["document"]["list"]:
	for l in t["element"]["attribute"]:
		if l["name"]=="Titulo_es":
			print l["text"]
