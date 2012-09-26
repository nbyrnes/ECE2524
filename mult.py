#ECE 2524 Homework 3 Problem 1 Nicholas Byrnes
#Multiplies numbers and calculates the product

import argparse
import sys

parser = argparse.ArgumentParser(description='Multiply Ints.')
parser.parse_args()

#initialize product for ease of use
product = 1

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

#end of program
		
