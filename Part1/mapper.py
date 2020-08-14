#!/usr/bin/env python

import sys
import csv

# input comes from STDIN
data = sys.stdin.readlines()
# parse the input we got from csv
reader = csv.reader(data)
# remove header
header = next(reader)
if header != None:
	for line in reader:
		# write result to STDOUT
		print '%s\t%s' % (line[9].capitalize(), 1)