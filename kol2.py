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

class Student:
	def __init__(self, name, surname):
		self.name = name
		self.surname = surname
		self.attendance = []
		self.scores = []
	def get_name(self):
		return self.name
	def get_surname(self):
		return self.surname
	def add_attendance(self, attendance):
		self.attendance.append(attendance)
	def add_score(self, score):
		self.scores.append(score)
	def get_score(self, class_number):
		return self.scores[class_number]
	def get_all_scores(self):
		return self.scores
	def get_attendance(self,class_number):
		return self.attendance[class_number]

class Class_group:
	def __init__(self):
		self.students = []
	def add_student(self, name, surname):
		self.students.append(Student(name, surname))
	def add_student_attendance(self, name, surname, attendance):
		for el in self.students:
			if el.get_name() == name and el.get_surname() == surname:
				el.add_attendance(attendance)
	def add_student_score(self, name, surname, score):
		for el in self.students:
			if el.get_name() == name and el.get_surname() == surname:
				el.add_score(score)
	def get_average_class_score(self, class_number):
		pass
	def get_total_average_score(self):
		number_of_scores = 0
		sum_of_scores = 0
		for el in self.students:
			sum_of_scores += sum(el.get_all_scores())
			number_of_scores += len(el.get_all_scores())
		return sum_of_scores/number_of_scores
	def get_total_attendance(self, class_number):
		sum_of_attendance = 0
		
		#return sum_of_attendance
	

class_group = Class_group()
class_group.add_student("John", "Doe")
class_group.add_student("John", "Smith")

class_group.add_student_attendance("John", "Smith", 1)
class_group.add_student_score("John", "Smith", 4)






