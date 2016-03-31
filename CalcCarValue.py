import pandas as pd
import numpy as np

#input variables:
Make = 'Toyota'
Model = 'Corolla'
Year = '2010'
Location = 'Johannesburg'
Millage = '100000'

#data validation:
DataValid = True

try:
	#python v2
	if not isinstance(Make, basestring):
		DataValid = False
except:
	#python v3
	if not isinstance(Make, str):
		DataValid = False
		
print(DataValid)

if DataValid is False:
	pass
else:
	
	Depfactors = pd.read_csv('DepreciationFactors.csv')


