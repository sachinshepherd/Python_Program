from scipy.stats.stats import pearsonr
import os, glob
import numpy as np

script_dir= os.path.dirname(os.path.realpath('__file__'))
path =  os.path.join(script_dir[0:-3],'yld_data/US_corn_grain_yield.txt')
path1= os.path.join(script_dir[0:-3],'answers/Correlations.out')
path2 =  os.path.join(script_dir[0:-3],'answers/YearlyAverages.out')
path3 =  os.path.join(script_dir[0:-3],'wx_data')
currentFile = glob.glob( os.path.join(path3, '*.txt'))
currentFile.sort()
outputfile=open(path1,'w')
ylist = []

fileList = []
for files in currentFile:
	fileList.append(files.split('/')[6])


file = open(path,'r')
for f in file.read().splitlines():
    ylist.append(int(f.split('\t')[1]))
print(ylist)

fil = open(path2,'r')
lines = fil.read().splitlines()
row_sets = [[c for c in line.split()] for line in lines] # read and split the lines in the columns
res=[]


for f in fileList:
	subset = [row for row in row_sets if row[0] == str(f)]
	res.append(subset)

for rs in res:
    list1 = []
    list2 = []
    list3 = []
    for r in rs:
        list1.append(float(r[2]))
        list2.append(float(r[3]))
        list3.append(float(r[4]))
    #print(list1)
    if len(list1) == len(ylist):
        c1 = format((pearsonr(list1,ylist)[0]), '.2f')
    if len(list2) == len(ylist):
        c2 = format((pearsonr(list2,ylist)[0]), '.2f')
    if len(list3) == len(ylist):
        c3 = format((pearsonr(list3,ylist)[0]), '.2f')
    outputfile.write(str(rs[0][0])+'\t'+str(c1)+'\t'+str(c2)+'\t'+str(c3)+'\n')