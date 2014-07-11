#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 10, 2014

@author: anroco

How to get the index of a substring contained in a python str looking
from the end of string?

¿Como obtener el indice de un substring contenido en un str python buscando
desde el final del string?
'''

#create a str
s = 'fresh fried fish, fish fresh fried'
print(s)

#the rfind() method return the index of the string where the
#last substring is found, return -1 if substring is not found.
index = s.rfind('fish')
print(index)

#define the segment of the string to perform the search
index = s.rfind('fish', 6, 18)
print(index)

#the rindex(value) method works like rfind() method, but raise ValueError
#when the substring is not found.
index = s.rindex('fresh')
print(index)

#difference between the two methods
print(s.rfind('not found'))
print(s.rindex('not found'))
