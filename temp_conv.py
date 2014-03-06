#!/usr/bin/env python
# -*- coding: utf-8 -*-

#temp_conv.py


#allows for float
from __future__ import division
#ask for tempature
print "Tempature Converter"
print ""
print ""
iinit_temp = raw_input ("What is the tempature? ")
print ""
temp_type = raw_input ("Is the tempature Fahrenheit(F), or Celsius (C)? Type the letter. ").lower
def temp_type():
	if temp_type == ("f"):
		conv_temp = init_temp-32
		conv_temp = conv_temp / 1.8
		print conv_temp
	if temp_type == ("c"):
		conv_temp = init_temp + 32
		conv_temp = init_temp * 1.8
		print conv_temp
	else:
		print "That is an invalid entry"
		
	
