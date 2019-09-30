####Homework 2 of CI class###
####Questino 2###
####min-min###
#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy
import numpy as np
import pandas as pd
from numpy import nan as NA

mintask = 0
p =0
data = np.array([[13 ,79, 23, 71, 60, 27 ,2],[31, 13, 14 ,94,60,61,57],[17,1,NA,23,36,8,86],[19,28,10,4,58,73,40],[94,75,NA,58,NA,68,46],[8,24,3,32,4,94,89],[10,57,13,1,92,75,29],[80,17,38,40,66,25,88]])

print(data, end='\n')
for i in range (0,8):
	#mintask = data.nanmin()
	#print (mintask,end='\n')
	p= np.nanargmin(data) #locate the minimum value
	x=p//7 # locate the task
	y=p%7 # locate the machine
	#print (mintask,p,x,y, end= '\n')

	print ("Step %d: Assign Task %d to machine %d"% (i,x, y), end ='\n')
	data[:,y] += data[x,y]
	data[x] =NA
	#print (data,end='\n')
	i=i+1
