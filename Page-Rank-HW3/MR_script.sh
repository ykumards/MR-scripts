# This script is for testing the python scripts
# on small input files before running it on hdfs cluster
# Run this from the project's root folder

./src/mapper.sh < input.txt | sort -k1,1 | ./src/reducer.sh


