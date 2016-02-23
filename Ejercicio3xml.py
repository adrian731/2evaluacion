#!/usr/bin/env python
#-*- coding: utf-8 -*-

from lxml import etree

accidents=etree.parse('accidentes.xml')
raiz=accidents.getroot()
accidentes=raiz.findall("result/accidente")


for a in accidentes:
	if int(a.find("afectado/afectado/age").text) <= 30:
		print a.find("afectado/afectado/age").text
		print a.find("afectado/afectado/type").text
		print a.find("afectado/afectado/status").text
	
		
	
