#!/usr/bin/env python
import csv
import re
import sys


while True:
    flag = 0
    print ("Enter the city name to be searched")
    print ("Enter any digit(0-9) to exit")
    phrase = raw_input();
    pattern = re.compile('[0-9]+')
    if (pattern.match(phrase)):
        sys.exit(0)
        break
    else:
        file = open('cityInformation','r')
        reader = csv.reader(file,delimiter='\t')

        for line in reader:
            if (phrase.capitalize() == line[0]):
                print (line[1])
                flag = 1
            
        
        if(flag == 0):
            print "City not found"
          
        file.close()

