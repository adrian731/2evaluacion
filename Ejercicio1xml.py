#!/usr/bin/env python
#-*- coding: utf-8 -*-

from lxml import etree

accidentes=etree.parse('accidentes.xml')
raiz=accidentes.getroot()
accidentes=raiz.findall("results/result")


for a in accidentes:	
	print a.find("type").text +"\n"+ a.find("reason").text +"\n"+ a.find("geometry/coordinates")
