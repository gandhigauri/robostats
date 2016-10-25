#!/usr/bin/env python
import IPython
import csv
from collections import namedtuple
from collections import defaultdict

def parser():
	OData = {}
	LData = {}
	with open('robotdata1.log') as f:
		lines = f.read().splitlines()
	f.close()

	for i,line in enumerate(lines):
		if lines[i][0] == 'L':
			l = lines[i].split()
			LData[i] = [float(l[x]) for x in range(1,len(l))]

		elif lines[i][0] == 'O':
			l = lines[i].split()
			OData[i] = (float(l[1]), float(l[2]), float(l[3]), float(l[4]))	

	return OData, LData

def main():
	OData, LData = parser()
	IPython.embed()

if __name__ == "__main__": 
	main()