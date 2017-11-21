# Filename: json2states.py
# Author: Dharmesh Tarapore <dharmesh@bu.edu>
# Description: Converts avro JSON to state JSON

import ast
import pyModeS as pms

INPUT_FILE = './temp.json'

# Open up the temp json file
with open(INPUT_FILE, 'rb') as f:
	stream = f.read()
	stream = stream.split('&')
	stream = stream.replace('null', 'None')
	streamDict = ast.literal_eval(stream)
	