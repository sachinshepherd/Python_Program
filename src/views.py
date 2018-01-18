import glob,os,re
from django.http import HttpResponse
import os.path
script_dir= os.path.dirname(os.path.realpath('__file__'))
path1 = os.path.join(script_dir[0:-3],'answers/MissingPrcpData.out')
path = os.path.join(script_dir[0:-3],'wx_data')
currentFile = glob.glob( os.path.join(path, '*.txt'))
count=0
currentFile.sort(key=lambda f: int(filter(str.isdigit, f)))
openfile1 = open(path1, 'w') 
for file in currentFile:
	x=file.split('/')[5]
	with open(file,'rb') as openfile:
		for line in openfile:
			count+=1
		openfile1.write(x+'\t'+str(count)+'\n')



	