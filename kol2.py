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

def create_student(name, surname):
    student = {'name':name, 'surname':surname, 'courses':{}}
    return student

def create_course(title, attendance):
    course = {'title':title, 'attendance':attendance}
    return course

def add_student_to_course(student, course):
    students_course = {'attendance':course['attendance']}
    students_course['actual_attendance'] = 0
    students_course['grades'] = []
    student['courses'][course['title']] = students_course

def mark_student(student, course, grade):
    courses = student['courses']
    if course['title'] not in courses:
        print 'Student does not atten given course!'
        return
    courses[course['title']]['grades'].append(grade)

def set_attendance(student, course, attendance):
    if attendance > course['attendance']:
        print 'Attendance can not be higher than amount of courses!'
        return
    student['courses'][course['title']]['actual_attendance'] = attendance

def increase_attendance(student, course):
    student['courses'][course['title']]['actual_attendance'] += 1

def get_average_score_in_class(student, course):
    grades = student['courses'][course['title']]['grades']
    return float(sum(grades))/len(grades)

def get_total_average_score(student):
    sum_of_grades = 0
    amount_of_grades = 0
    for course in student['courses'].values():
        sum_of_grades += sum(course['grades'])
        amount_of_grades += len(course['grades'])
    return float(sum_of_grades)/amount_of_grades

def get_total_attendance(student):
    max_attendance = 0
    actual_attendance = 0
    for course in student['courses'].values():
        max_attendance += course['attendance']
        actual_attendance += course['actual_attendance']
    return float(actual_attendance)/max_attendance

if __name__ == '__main__':
    student1 = create_student('John', 'Smith')
    course1 = create_course('biology', 30)
    course2 = create_course('physics', 28)

    add_student_to_course(student1, course1)
    add_student_to_course(student1, course2)

    mark_student(student1, course1, 3)
    mark_student(student1, course1, 4)
    mark_student(student1, course2, 3)

    set_attendance(student1, course1, 25)
    increase_attendance(student1, course2)

    print student1
    print course1
    print get_average_score_in_class(student1, course1)
    print get_total_average_score(student1)
    print get_total_attendance(student1)

