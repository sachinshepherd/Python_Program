import glob,os,re
import os.path
import sys
import matplotlib.pyplot as plt
import numpy as np
from pandas import *


script_dir= os.path.dirname(os.path.realpath('__file__'))
path2 =  os.path.join(script_dir[0:-3],'wx_data')
currentFile = glob.glob( os.path.join(path2, '*.txt'))
currentFile.sort()
path =  os.path.join(script_dir[0:-3],'answers/YearlyAverages.out')
path1= os.path.join(script_dir[0:-3],'answers/YearHistogram.out')
#currentFile = glob.glob( os.path.join(path, '*') )
fileList = []
outputfile=open(path1,'w')
for files in currentFile:
	fileList.append(files.split('/')[6])


#files.split('/')[5]
file = open(path,'r')
lines = file.read().splitlines()
row_sets = [[c for c in line.split()] for line in lines] # read and split the lines in the columns
res=[]

for f in fileList:
	subset = [row for row in row_sets if row[0] == str(f)]
	res.append(subset)
dicc = {}
for r in res:

	maxT = -sys.maxsize
	minT = sys.maxsize
	total = 0
	dicc[r[0][0]] = {}
	for result in r:
		if maxT < float(result[2]):
			maxT = max(maxT, float(result[2]))
			tempMax = result[1]
		if minT > float(result[3]):
			minT = min(minT,float(result[3]))
			tempMin = result[1]
		if total < float(result[4]):
			total = max(total,float(result[4]))
			tempTotal = result[1]
	dicc[r[0][0]]['max'] = tempMax
	dicc[r[0][0]]['min'] = tempMin
	dicc[r[0][0]]['total'] = tempTotal
print(dicc)
ans = {}
for year in range(1985,2015):
	maxtotal = 0
	mintotal = 0
	ptotal = 0
	for v in dicc.values():
		if v['max'] == str(year):
			maxtotal = maxtotal + 1
		if v['min'] == str(year):
			mintotal = mintotal + 1
		if v['total'] == str(year):
			ptotal = ptotal + 1
	outputfile.write(str(year)+'\t'+str(maxtotal)+'\t'+str(mintotal)+'\t'+str(ptotal)+'\n')
	ans[str(year)] = [maxtotal,mintotal,ptotal]


#di = {'facebook':[2,3,4,6],'Twitter':[1,2,3,3],'Instagram':[4,5,6,7],'Tumblr':[5,7,8,9]}
df = DataFrame(ans)
df.plot(kind='bar', color='rbmcy')
plt.show()
