# Map-Reduce

## File transfer to VM(already copied in cs4417-lab-5)

sftp -i cs4417-lab-5.pem cloudera@cs4417-lab-5.gaul.csd.uwo.ca


## Transfer the input files first(already copied in cs4417-lab-5)

put starbucks-locations-sort.csv

put movies.dat


## Transfer the code files

put Part1.zip

put Part2.zip

put Part3.zip

exit


## Login to VM

ssh -i cs4417-lab-5.pem cloudera@cs4417-lab-5.gaul.csd.uwo.ca


### Create input directory in hdfs(already created in cs4417-lab-5)

hadoop fs -mkdir /user/cloudera/inputAssignment1


### Create sub-directory to place the input files

hadoop fs -mkdir /user/cloudera/inputAssignment1/Starbucks

hadoop fs -mkdir /user/cloudera/inputAssignment1/Movies


### Copy input files to hdfs(already copied in cs4417-lab-5)

hadoop fs -copyFromLocal starbucks-locations-sort.csv /user/cloudera/inputAssignment1/Starbucks/starbucks-locations-sort.csv

hadoop fs -copyFromLocal movies.dat /user/cloudera/inputAssignment1/Movies/movies.dat


### Display list of files in hdfs

hadoop fs -ls /user/cloudera/inputAssignment1/Starbucks/

hadoop fs -ls /user/cloudera/inputAssignment1/Movies/


### Unzip all the code files

unzip Part1.zip

unzip Part2.zip

unzip Part3.zip


## Execute Part1

cd Part1

### Run hadoop job for Part1

hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.6.0-mr1-cdh5.12.0.jar -mapper mapper.py -file mapper.py -reducer reducer.py -file reducer.py -input /user/cloudera/inputAssignment1/Starbucks -output /user/cloudera/outputAssignment1/Starbucks

### Display Reducer output

hadoop fs -cat /user/cloudera/outputAssignment1/Starbucks/*

### Write Reducer output to a file(required)

hadoop fs -getmerge /user/cloudera/outputAssignment1/Starbucks/* cityInformation

### Execute the query(reads the cityInformation file)

python query.py

### Remove output folder(if needed)

hadoop fs -rm /user/cloudera/outputAssignment1/Starbucks/*

hadoop fs -rmdir /user/cloudera/outputAssignment1/Starbucks


## Execute Part2

cd ..

cd Part2


### Execute the indexer(Reads the input file from '/home/cloudera/' path)

python indexer.py


### Execute the query

python query.py


## Execute Part3

cd ..

cd Part3


### Run hadoop job for Part3

hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.6.0-mr1-cdh5.12.0.jar -mapper mapper.py -file mapper.py -reducer reducer.py -file reducer.py -input /user/cloudera/inputAssignment1/Movies -output /user/cloudera/outputAssignment1/Movies


### Display Reducer output

hadoop fs -cat /user/cloudera/outputAssignment1/Movies/*


### Write Reducer output to a file(required


hadoop fs -getmerge /user/cloudera/outputAssignment1/Movies/* invertedIndex

### Execute the query(reads the invertedIndex file)
python query.py


### Remove output folder(if needed)

hadoop fs -rm /user/cloudera/outputAssignment1/Movies/*

hadoop fs -rmdir /user/cloudera/outputAssignment1/Movies
