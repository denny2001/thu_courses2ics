from config import XLS_PATH, ICS_PATH
from list2ical import icalWriter
from xls2list import CourseLogger

if __name__ == '__main__':
    logger = CourseLogger(XLS_PATH)
    course_list = logger.parse_to_list()

    writer = icalWriter(ICS_PATH)
    writer.add_courses_to_cal(course_list)
    print('file generation success')
