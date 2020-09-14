import numpy as np
import pyexcel as p
from course import Course
from config import XLS_PATH


class CourseLogger(object):
    def __init__(self, xls_path):
        super().__init__()
        self.xls_path = xls_path
        self.courses_np = np.array([])
        self._get_records()
        self.list_of_courses = []

    def _get_records(self):
        records = np.array(p.get_sheet(file_name=self.xls_path))
        self.courses_np = records[2:8, 1:8]

    def _string2span(self, string):
        if '全周' in string:
            return 1, 16
        elif '前八周' in string:
            return 1, 8
        elif '后八周' in string:
            return 9, 16
        else:
            return tuple(map(int, string[:-1].split('-')))

    def _parse_course_string(self, string):
        string = str(string)
        assert isinstance(string, str)
        if '\n' in string:
            return [self._parse_course_string(s) for s in string.split('\n')]

        course_name = '('.join(string.split('；')[0].split('(')[:-1])
        lecturer = string.split('；')[0].split('(')[-1]

        location = string.split('；')[-1][:-1]
        week_span = self._string2span(string.split('；')[-2])

        # exceptions:
        if '候选' in string:
            location = '未知'
            week_span = self._string2span(string.split('；')[-1])

        return course_name, lecturer, week_span, location
        # return Course(name=course_name, lecturer=lecturer, week_span=week_span, location=location)

    def _log(self):
        for num, course_string in enumerate(np.nditer(self.courses_np)):
            if not course_string:
                continue

            section = (num % 7 + 1, num // 7 + 1)
            course_name, lecturer, week_span, location = self._parse_course_string(course_string)

            course = Course(name=course_name, lecturer=lecturer, section=section, week_span=week_span, location=location)
            self.list_of_courses.append(course)

            print(f'{course} filed successfully')

    def parse_to_list(self):
        self._log()
        return self.list_of_courses
