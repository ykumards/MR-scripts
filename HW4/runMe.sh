echo "Running the Pig Script"

pig -x local script1.pig

echo "Pretty Printing using Python"

touch output.txt
python prettyPrint.py

echo "Done."
