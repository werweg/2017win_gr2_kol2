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

#! /usr/bin/env python2.7

class Course():
	def __init__(self, name, number_of_classes):
		self.name = name
		self.number_of_classes = number_of_classes

	def __str__(self):
		return self.name

	def get_number_of_classes(self):
		return number_of_classes

class StudentsCourse():
	def __init__(self, course):
		self.course = course
		self.grades = []
		self.attendance = 0

	def add_grade(self, grade):
		self.grades.append(grade)

	def get_average(self):
		return sum(self.grades)/len(self.grades)

	def set_attendance(self, attendance):
		self.attendance = attendance

	def get_percentage_of_attendance(self):
		return attendance*100/self.course.get_number_of_classes()


class Student():
	def __init__(self, name, surname):
		self.name = name
		self.surname = surname
		self.courses = []

	def __str__(self):
		return '%s %s' % (self.surname, self.name)

	def add_students_course(students_course):
		self.courses.append(students_course)

	def get_total_average(self):
		totalSum = 0
		for course in courses:
			tutalSum += course.get_average()
		return totalSum/len(courses)

	def get_attendance_at_course(self, course):
		if course not in self.courses:
			print 'Student is not attending %s course' % (course)
		else:
			x=0


if __name__ == '__main__':
	course1 = Course('biology', 20)
	print course1


	student1 = Student('John', 'Smith')
	print student1


