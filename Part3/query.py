import sys
import re
import csv

class Movie:
    
    def searcher(self):
        print "Enter the Query to be searched either as : <word> or <word1> <operator> <word2>"
        print "Enter any digit(0-9) to exit"
        phrase = raw_input();
        pattern = re.compile('[0-9]+')
        if (pattern.match(phrase)):
            sys.exit(0)
        else:
            self.searchMovie(phrase)
    
    def searchMovie(self,phrase):
        
        word_list = phrase.split(' ')
        movie_list = []
        
        movie_dict = {}
        
        with open('invertedIndex') as f:
            lineList = f.readlines()
        
        for i in range(0,len(lineList)):
            genre,mov = lineList[i].split('\t')
            mov = mov[:-1]
            movie_list = mov.split('|')
            movie_dict[genre] = movie_list
        
        data = dict((key.lower(),value) for key,value in movie_dict.items())
         
         
        if(len(word_list) == 1):
            result_list = data.get(word_list[0].lower())
            if (not result_list):
                print "Genre Does Not Exists"
            else:
                for result in result_list:
                    print result
        else:
            if(word_list[1].lower() == 'and'):
                temp_list1 = data.get(word_list[0].lower())
                temp_list2 = data.get(word_list[2].lower())
                
                if(not temp_list1 or not temp_list2):
                    print "Genre Does Not Exists"
                else:
                    result_list = set(temp_list1).intersection(temp_list2)
                    if(not result_list):
                        print "No Movies found"
                    else:
                        for result in result_list:
                            print result
                
                
            elif(word_list[1].lower() == 'or'):
                temp_list1 = data.get(word_list[0].lower())
                temp_list2 = data.get(word_list[2].lower())
                if(not temp_list1 or not temp_list2):
                    print "Genre Does Not Exists"
                else:
                    concatenated_list = temp_list1 + temp_list2
                    result_list = set(concatenated_list)
                    if(not result_list):
                        print "No Movies found"
                    else:
                        for result in result_list:
                            print result

if __name__ == '__main__':
    Movie().searcher()    