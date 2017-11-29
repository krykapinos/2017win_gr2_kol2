# Class diary  
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
# The default interface for interaction should be python interpreter.
# Please, use your imagination and create more functionalities. 
# Your project should be able to handle entire school.
# If you have enough courage and time, try storing (reading/writing) 
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface.


#!/usr/bin/env python2

from optparse import OptionParser
import json
import os.path


def read_data_from_file(filename):
    if os.path.isfile(filename):
	file_dictionary = {}
        with open(filename, 'r') as file:
            file_dictionary = json.load(file)
        return file_dictionary
    else:
	return {}

def save_data_to_file(dictionary, filename):
    with open(filename, 'w') as file:
        json.dump(dictionary, file)

def add_student(diary, name, surname):
    diary.setdefault(name+surname, {'Name': name, 'Surname': surname, 'Classes': {}})

def add_student_attendance(diary, name, surname, class_name, attendance):
    diary[name+surname]['Classes'].setdefault(class_name, {'Attendance': [], 'Score': []} )
    diary[name+surname]['Classes'][class_name]['Attendance'].append(attendance)

def add_student_score(diary, name, surname, class_name, score):
    diary[name+surname]['Classes'].setdefault(class_name, {'Attendance': [], 'Score': []} )
    diary[name+surname]['Classes'][class_name]['Score'].append(score)

def get_student_total_average(diary, name, surname):
    counter, average = 0., 0.
    for dict_key in diary[name+surname]['Classes'].keys():
        counter += len(diary[name+surname]['Classes'][dict_key]['Score'])
        average += sum(diary[name+surname]['Classes'][dict_key]['Score'])
    return average/counter

def get_students_average(diary, class_name):
    counter, average = 0., 0.
    for dict_key in diary.keys():
        counter += len(diary[dict_key]['Classes'][class_name]['Score'])
        average += sum(diary[dict_key]['Classes'][class_name]['Score'])
    return average/counter

def get_total_attendance(diary, class_name):
    attendance = 0
    for dict_key in diary.keys():
        attendance  += sum(diary[dict_key]['Classes'][class_name]['Attendance'])
    return attendance


if __name__ == "__main__":

    parser = OptionParser()
    parser.add_option("-f", "--file", dest="filename", default='class_diary.json',
		 help="Write/read data to/from FILE", metavar="FILE")
    parser.add_option("-w", "--write", action="store_true", dest="only_write", default=False,
                 help="Only write to FILE")

    (options, args) = parser.parse_args()

    diary = {}
    if options.only_write == False:
        diary = read_data_from_file(options.filename)

    add_student(diary, 'Jan', 'Kowalski')
    add_student(diary, 'Jan', 'Nowak')
    add_student_attendance(diary, 'Jan', 'Kowalski', 'class1', 1)
    add_student_attendance(diary, 'Jan', 'Kowalski', 'class2', 0)
    add_student_attendance(diary, 'Jan', 'Nowak', 'class1', 1)
    add_student_score(diary, 'Jan', 'Kowalski', 'class1', 4.)
    add_student_score(diary, 'Jan', 'Kowalski', 'class1', 4.)
    add_student_score(diary, 'Jan', 'Kowalski', 'class2', 3.)
    add_student_score(diary, 'Jan', 'Nowak', 'class1', 5.)
    print("Jan Kowalski average = {:.2f}".format(get_student_total_average(diary, 'Jan', 'Kowalski')))
    print("All students average from class1 = {:.2f}".format(get_students_average(diary, 'class1')))
    print("Students attendance at class1 = {:d}".format(get_total_attendance(diary, 'class1')))

    save_data_to_file(diary, options.filename)
