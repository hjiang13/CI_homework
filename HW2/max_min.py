####Homework 2 of CI class###
####Questino 2###
####max-min###
#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy
import numpy as np
import pandas as pd
from numpy import nan as NA

mintask = 0
q =0
data = np.array([[13 ,79, 23, 71, 60, 27 ,2],[31, 13, 14 ,94,60,61,57],[17,1,NA,23,36,8,86],[19,28,10,4,58,73,40],[94,75,NA,58,NA,68,46],[8,24,3,32,4,94,89],[10,57,13,1,92,75,29],[80,17,38,40,66,25,88]])

print(data, end='\n')
for i in range (0,8):
	p= np.nanargmin(data,axis=1) # to find the min value in every row/task
#	print (p)
	cache = np.array([0,0,0,0,0,0,0,0]) # store all the minimums into a array
	for j in range (0,8):
		cache[j] = data[j,p[j]]
#	print (cache)
	task = np.argmax(cache) # loocate the maxmum 
#	print (task)
	machine = p[task]
#	print (machine)

	print ("Step %d: Assign Task %d to machine %d"% (i,task , machine), end ='\n')
	data[:,machine] += data[task,machine]
	data[task,:] = 0
#	print (data,end='\n')
	i=i+1

