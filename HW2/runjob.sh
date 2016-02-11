#!/bin/bash

# Program exits after a line fail
#set -e

echo "Locating streaming jar file..."
export HADOOP_HOME=/opt/cloudera/parcels/CDH-5.4.5-1.cdh5.4.5.p0.7/

echo "Removing existing out file..."
hadoop fs -rm -r spawn.out

echo "How many reducers to spawn?"
read redNo

hadoop jar $HADOOP_HOME/lib/hadoop-mapreduce/hadoop-streaming.jar -D mapred.reduce.tasks=$redNo -file `pwd`/src -mapper src/mapper.sh -reducer src/reducer.sh -input input.txt -output spawn.out

echo "It's better to change the output name...Enter a name:"
read name

hadoop fs -cp spawn.out $name.out

