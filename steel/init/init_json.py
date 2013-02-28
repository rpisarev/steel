#!/usr/bin/env python
import os.path
import json
import string
import time

def read_group(filename):
	f = open(filename, 'r')
	first_line = f.readline()
	if first_line != 'Group\n':
		print("Error format group")
		return -1
	lines = f.readlines()
	group_list = []
	for record in lines:
		record = record.rstrip()
		group_list += [record.split('\t')]
	return group_list

def read_student(filename):
         f = open(filename, 'r')
         first_line = f.readline()
         if first_line != 'Student\n':
                print("Error format student")
                return -1
         lines = f.readlines()
         student_list = []
         for record in lines:
		record1 = record.rstrip().split('\t')
		record1[1] = time.strftime("%Y-%m-%d", time.strptime(record1[1], "%m/%d/%Y"))
                student_list += [record1]
         return student_list

def gen_data(groups, students):
	data = {}
	if groups != -1 and students != -1:
		data['groups'] = groups
		data['students'] = students
		return data
	else:
		print("Error initiation")
		return -1

def gen_json(file_group, file_student):
	data = gen_data(read_group(os.path.join(os.path.dirname(__file__), file_group)), read_student(os.path.join(os.path.dirname(__file__), file_student)))
	if data != -1:
		return json.dumps(data)
	else:
		return -1

def save_json(file_json):
	jsonfile = open(os.path.join(os.path.dirname(__file__), file_json), 'w')
	data = gen_json('init_group.txt', 'init_student.txt')
	if data != -1:
		jsonfile.write(data)
		return 0
	else:
		print("Can't create JSON")
		return -1
print save_json('initial_data.json')























