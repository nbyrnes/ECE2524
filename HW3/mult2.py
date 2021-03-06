#ECE 2524 Homework 3 Problem 2 Nicholas Byrnes
#Multiplies numbers and calculates the product while accepting command line arguments

import argparse
import sys

parser = argparse.ArgumentParser(description='Multiply Ints.')
parser.add_argument('filename', metavar='F', type-str, nargs='*', help='filename')
parser.add_argument('--ignore-blank', dest='iblank', action='store_const', const='1', default='0', help='Ignore blank spaces')
parser.add_argument('--ignore-non-numeric',dest='-inn', action = 'store_const', const='1', default='0', help='Ignore lines that don\'t contain integers')

args = parser.parse_args()

#initialize product for ease of use
product = 1

if len(args.filename) == 0:
	#stay in loop till told to exit
	while 1:
		try:
			#reads in input
			num = sys.stdin.readline()
			
			#checks for special situations
			if num == '':
				raise KeyboardInterrupt
			if num == '^D':
				raise KeyboardInterrupt
			if num == '\n':
				raise EOFError
			newProduct = int(num)
			product = newProduct * product
			
		#built in exception keywords to cover necessary implementations
		except KeyboardInterrupt:
			print(product)
			sys.exit(0)
		except ValueError:
			sys.stderr.write("ERROR: Incorrect Format!\n")
			sys.exit(1)
		except EOFError:
			print(product)
else:
	while (len(args.filename) != 0):
		x = args.filename.pop()
		for nstring in fileinput.input(x):
			if args.inn == '1':
				if nstring != '\n':
					try:
						test = int(nstring)
					except ValueError:
						nstring = '1'
			if nstring == '\n':
				if args.iblank =='1':
					nstring = '1'
				else:
					print(product)
					nstring = '1'
					product = 1
			newNewProduct = int(nstring)
			product = newNewProduct * product
	print(product)
			
#end of program
		
