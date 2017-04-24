#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv

file = "bus.csv"
bus_id = 23
day_type = 3
origin = "Roças Grandes"
destiny = "Belo Horizonte"

def read_file(file_name):
    reader = csv.reader(open(file_name, "rb"), delimiter=",")
    return list(reader)


def column(matrix, i):
    return [row[i] for row in matrix]

def format_number(num):
	if int(num) > 9:
		return str(num)
	return "0"+str(num)

def format_time(hour, minute):
	return "%s:%s:00" % (format_number(hour), format_number(minute))


def column_parser(col):
	hour = col[0]
	for value in col[1:]:
		if value:
			time = format_time(hour, value)
			print "(%d, %d, '%s', '%s', null, '%s')," % (bus_id, day_type, origin, destiny, time)

schedules = read_file( file )
num_schedules = len(schedules[0])
print "INSERT INTO `schedule` (`bus_id`, `daytype_id`, `origin`, `destiny`, `observation`, `time`) VALUES"
for i in range(0, num_schedules):
	column_parser(column(schedules, i))
