#!/usr/bin/env python
import IPython
import os.path
import sys
from collections import namedtuple
from collections import defaultdict

def parser():
	OData = {}
	LData = {}
	basePath = os.path.dirname(__file__)
	filePath = os.path.abspath(os.path.join(basePath,"..","..","robotdata1.log"))
	f = open(filePath,"r")
	#with open('robotdata1.log') as f:
	lines = f.read().splitlines()
	f.close()

	for i,line in enumerate(lines):
		if lines[i][0] == 'L':
			l = lines[i].split()
			LData[i] = tuple(float(l[x]) for x in range(1,len(l)))

		elif lines[i][0] == 'O':
			l = lines[i].split()
			OData[i] = tuple(float(l[x]) for x in range(1,len(l)))	

	return OData, LData

def main():
	OData, LData = parser()
	IPython.embed()

if __name__ == "__main__": 
	main()