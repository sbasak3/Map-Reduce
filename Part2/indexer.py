#!/usr/bin/env python
import sys
import csv
import json

inverted_index = {}
movies = []
genre = []

# making data frame from csv file  
file = open('/home/cloudera/movies.dat','r')
reader = csv.reader((line.replace('::', '\t') for line in file), delimiter='\t')   

for line in reader:
    movies.append(line[1])
    split_data = line[2].split("|")
    genre.append(split_data)


for i in range(0,len(movies)):
    if (genre[i] == ['']):
        if 'None' in inverted_index:
            inverted_index['None'].append(movies[i])
        else:
            inverted_index['None'] = [movies[i]]
    else:
        for j in range(0,len(genre[i])):
            if genre[i][j] in inverted_index:
                inverted_index[genre[i][j]].append(movies[i])
            else:
                inverted_index[genre[i][j]] = [movies[i]]

with open('invertedIndex.json', 'w') as fp:
    json.dump(inverted_index, fp)