#!/usr/bin/env python
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
import json
import settings
import time
#import string
from kiwi.models import Group, Student

def load_json(file_json):
	try:
		jsonfile = open(os.path.join(os.path.dirname(__file__), file_json), 'r')
		data = json.loads(jsonfile.readline())
		return data
	except:
		print("Error reading JSON")
		return -1

def gen_group(elem_group):
	name, starosta = elem_group
	return Group(name = name)

def gen_student(elem_student, group):
	fio, birth, number = elem_student
	try:
		number = int(number)
	except:
		number = 0
	return Student(fio = fio, birth = birth, number = number, group = group)

def create_group_and_student(data):
	if data != -1:
		groups_list = data['groups']
		groups = {}
		res = {}
		students ={}
		for elem in groups_list:
			groups[elem[0]] = gen_group(elem)
		students_list = data['students']
		for elem in students_list:
			students[elem[0]] = gen_student(elem[:-1], groups[elem[-1]])
		for elem in groups_list:
			groups[elem[0]].add_starosta(students[elem[1]])
		res['groups'] = groups.values()
		res['students'] = students.values()
		return res
		
	else:
		return -1


def init_models(models_dict):
	if models_dict != -1:
		for obj in models_dict['groups']:
			obj.save()
		for obj in models_dict['students']:
		        obj.save()
		return "Ok!"
	else:
		print("Sorry, can't create models elemetnts")
		return -1


print init_models(create_group_and_student(load_json('initial_data.json')))

















