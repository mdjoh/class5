#!/usr/bin/env python

# 1. load a dataset from a file
# 2. "organize" that file, so we can access columns or rows of it easily
# 3. Compute some "summary stats" about the dataset
# 4. print those summary stats

# 1. load a dataset
# 1a. accept arbitrary filename as argument
# 1b. load the file

from argparse import ArgumentParser

parser = ArgumentParser(description = 'A CSV reader + stats maker')
parser.add_argument ('csvfile',
		type=str,
		help='Path to the input csv file.')

parsed_args = parser.parse_args()
# sys arg v is not recommended

#print(parsed_args)
#print(parsed_args.csvfile)

my_csv_file = parsed_args.csvfile

# check if the file being passed exists

import os
import os.path as op

#solution 1
#if os.path.isfile(my_csv_file):
#	print("file is real")
#else:
#	print("not a file")

# stop program running and display a message when an error is encountered 

# original solution:
assert op.isfile(my_csv_file), "give real file please"

#solution 3
#if not os.path.isfile(my_csv_file):
#	raise ValueError("not a file. give real file")

print('file is there!')


# Part 1b. load the file
import pandas as pd

#piped separator; this case its 1 or more spaces or comma
data = pd.read_csv(my_csv_file, sep='\s+|,' ,header=None)
print(data.head())

#display dir items for data
#for item in dir(data):
#	print(item)

print(data.shape)


# 2. organize data and access row, column, or specific value easily

# rows 4 and 5:
#print(data.iloc[3:5,:])

# 1st 3 rows and last 3 col:
#print(data.iloc[:3, -3:])

# specific value:
#print(data.iloc[3,4])

# Computing and printing summary stats
import numpy as np

print(np.mean(data))
print(np.std(data))
