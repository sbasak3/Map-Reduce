#!/usr/bin/env python

import sys
import csv

# input comes from STDIN
data = sys.stdin.readlines()
# parse the input we got from movies.dat
reader = csv.reader((line.replace('::', '\t') for line in data), delimiter='\t')

movies = []
genre = []

for line in reader:
    movies.append(line[1])
    split_data = line[2].split("|")
    genre.append(split_data)

for i in range(0,len(movies)):
    if (genre[i] == ['']):
    	print '%s\t%s' % ("None", movies[i])
    else:
        for j in range(0,len(genre[i])):
        	print '%s\t%s' % (genre[i][j], movies[i])