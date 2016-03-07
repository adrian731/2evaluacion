#!/usr/bin/env python
#-*- coding: utf-8 -*-
import json
trabajo=open("trabajo.json","r")    
trabajos=json.load(trabajo)



for t in trabajos["document"]["list"]:
	for l in t["element"]["attribute"]:
		if l["name"]=="Provincia":
				provincias.append(l["valor"][0]["string"])
			
for p in provincias:
	if nombres.count(p)==0:
		print p, provincias.count(p)
		nombres.append(p)
