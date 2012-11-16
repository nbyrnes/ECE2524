#Nicholas Byrnes, ECE 2524, HW4

import argparse
import sys
import csv
import ast

data = []

#adds a part to database
def insert_data(data, args):
	data.append(ast.literal_eval(args))
	print("Inserted a data entry.")
	
#remove a part from the database
def delete_data(data, args):
	ID, value = args.split('=', 1)
	#checks for valid entry
	if ID not in fields:
		print("ERROR: Not a valid entry!".format(ID), file=sys.stderr) 
		return
	deleted = []
	for row in data:
		if row[ID] == value:
			deleted.append(row)
	for row in deleted:
		data.remove(row)
	print("Deleted a data entry.")

#set/update specific values in the databse
def update_data(data, args):
	update, condition = args.split(' where ', 1) #action
	update_ID, update_value = update.split('=', 1)
	cond_ID, cond_value = condition.split('=', 1)
	if update_ID not in fields:
		print("Error: Not a valid entry!".format(update_ID), file=sys.stderr)
		return
	if cond_ID not in fields:
		print("Error: Not a valid entry!".format(cond_ID), file=sys.stderr)
		return
		if update_ID == 'Quantity':
			update_value = int(update_value)
		if cond_ID == 'Quantity':
			cond_value = int(cond_value)
			
	newEntries = 0
	for row in data:
		if row[cond_ID] == cond_value:
			row[update_ID] = update_value
			updated = updated + 1
			
	print("Updated data entries")
	
#sort the records by a specific field name
def sort_data(data, args):
	if ' sort by ' in args:
		args, sort_field = args.split(' sort by ', 1)
		data = sorted(data, ID = lambda x: x[sort_field])
		
	condition = lambda x: True
	if ' where ' in args:
		args, cond = args.split(' where ', 1)
		cond_ID, cond_value = condition.split('=', 1)
		if cond_ID == 'Quantity':
			cond_value = int(cond_value)
		cond = lambda x: x[cond_ID] == cond_val
	data = filter(cond, data)
	for row in data:
		print(row)
		
	print("Sorted and listed records")

dataInputs = []
commands = {
	'insert': insert_data, 
	'delete': delete_data,
	'update': update_data,
	'select': sort_data,
}

#defines the main() function
def main():
	parser = argparse.ArgumentParser('Reads in files upon startup and waits for CLAs')
	parser.add_argument('-f', '--data-file', metavar='file', help='Filename needed for startup')

	args = parser.parse_args()
	
	global data, dataInputs
	with open(args.data_file) as f:
		reader = csv.DictReader(f, doubleQuote=False, escapechar='\\', quoting=csv.QUOTE_NONNUMERIC)
		dataInputs = reader.dataNames
		data = [value for value in reader]
		
	for row in data:
		row['Quantity'] = int(row['Quantity'])
	
	for line in iter(sys.stdin.readline, ""):
		cmd = line.rstrip('\n').split(None, 1)
		if len(cmd) > 1:
			rest = cmd[1]
		else:
			rest = ' '
			cmd = cmd[0]
			if cmd in commands:
				commands[cmd](data, rest)
			else:
				print("ERROR: Incorrect Command: '{}'.".format(cmd), file sys.stderr)

#parses CLAs and calls functions to parse data and commands
if __name__ == "__main__":
	main()

