from typing import List
from functools import reduce


def get_top(data: List[dict]) -> dict:
    """Returns top student name by course"""
    top_students = {}
    for i in data:
        if (i['course'] not in top_students) or (i['rate'] > top_students[i['course']]['rate']):
            top_students[i['course']] = i
    return dict(map(lambda c: (c, top_students[c]['name']), top_students))

    # ----------------------------------------------------

    # courses = list(set(item['course'] for item in data))
    # students_courses = {}
    # # group students by course
    # for course in courses:
    #     students_courses[course] = []
    #     for student in data:
    #         if student['course'] == course:
    #             students_courses[course].append(student)

    # top_students = {}
    # for course, students in students_courses.items():
    #     top_student = max(students, key=lambda s: s['rate'])
    #     top_students[course] = top_student['name']
    
    # return top_students
