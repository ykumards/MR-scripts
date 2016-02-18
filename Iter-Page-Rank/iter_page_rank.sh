#!/bin/bash
# Script to run Page Rank iteratively (hardcoded to 3 iterations)

# Program exits after a line fail
#set -e

echo "Locating streaming jar file..."
export HADOOP_HOME=/opt/cloudera/parcels/CDH-5.4.5-1.cdh5.4.5.p0.7/

echo "Loading input file"

hdfs dfs -cp -f input.txt iter_input.txt

 
for counter in `seq 1 3`; do

	echo "Removing existing out file..."
	hdfs dfs -rm -r spawn.out

	echo "Iteration Number:"
	echo $counter

	hadoop jar $HADOOP_HOME/lib/hadoop-mapreduce/hadoop-streaming.jar -D mapred.reduce.tasks=1 -file `pwd`/src -mapper src/mapper.sh -reducer src/reducer.sh -input iter_input.txt -output spawn.out

	hdfs dfs -cp -f spawn.out/part-00000 iter_input.txt
        hdfs dfs -cat iter_input.txt
done

echo "Fetching output..."
rm iter_input.txt
hdfs dfs -get iter_input.txt
