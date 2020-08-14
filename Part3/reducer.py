#!/usr/bin/env python

from operator import itemgetter
import sys

current_genre = None
current_movie = None
genre = None



# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    genre, movie = line.split('\t', 1)

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: genre) before it is passed to the reducer
    if current_genre == genre:
        current_movie = current_movie + '|' + movie
    else:
        if current_genre:
            # write result to STDOUT
            print '%s\t%s' % (current_genre, current_movie)
        current_movie = movie
        current_genre = genre

# do not forget to output the last movie if needed!
if current_genre == genre:
    print '%s\t%s' % (current_genre, current_movie)

