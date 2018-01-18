import os, glob
import re

script_dir= os.path.dirname(os.path.realpath('__file__'))
path =  os.path.join(script_dir[0:-3],'wx_data')
path1= os.path.join(script_dir[0:-3],'answers/MissingPrcpData.out')
currentFile = glob.glob( os.path.join(path, '*.txt'))
currentFile.sort()
outputfile=open(path1,'w')
for files in currentFile:
	files.split('/')[5]
	file = open(files,'r')
	lines = file.read().splitlines()
	row_sets = [[c for c in line.split()] for line in lines] # read and split the lines in the columns
	res=[]
	count = 0
	for line in row_sets:
		if int(line[1]) != -9999 and int(line[2]) != -9999 and int(line[3]) == -9999:
			count = count + 1
	outputfile.write(files.split('/')[6]+'\t'+str(count)+'\n')

