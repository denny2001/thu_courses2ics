from course import Course
from icalendar import Calendar, Event
from config import ICS_PATH, START_OF_SEMESTER, SECTION_TIME
from datetime import datetime, timedelta


def parse_section_time(section_time):
    """
    a utility function. transform string-formatted time to datetime format
    """
    output = []
    for section in section_time:
        output.append([timedelta(hours=int(t.split(':')[0]), minutes=int(t.split(':')[1])) for t in section])
    return output


class icalWriter(object):
    def __init__(self, ics_path=ICS_PATH, start_date=START_OF_SEMESTER, section_time=SECTION_TIME, tz='Asia/Shanghai'):
        self.start_date = datetime(*map(int, start_date.split('-')))
        self.end_date   = self.start_date + timedelta(weeks=16)
        self.tz = tz
        self.ics_path = ics_path
        self.section_time = section_time

        self.cal = Calendar()
        self.cal.add('version', 2.0)
        self.cal.add('calscale', 'GEORGIAN')

    def course2event(self, course: Course):
        times = parse_section_time(self.section_time)
        start_time = self.start_date + timedelta(weeks=course.week_span[0]-1, days=int(course.section[0])-1) + times[course.section[1]-1][0]
        end_time   = self.start_date + timedelta(weeks=course.week_span[0]-1, days=int(course.section[0])-1) + times[course.section[1]-1][1]

        event = Event()
        # critical info
        event.add('summary', course.name)
        event.add('location', course.location)
        event.add('dtstart', start_time, parameters={'tzid': self.tz})
        event.add('dtend', end_time, parameters={'tzid': self.tz})
        event.add('rrule', {'freq': 'weekly', 'until': self.end_date})

        # misc info
        event.add('sequence', 0)

        return event

    def add_courses_to_cal(self, courses: [Course]):
        for course in courses:
            self.cal.add_component(self.course2event(course))
        with open(self.ics_path, 'wb') as f:
            f.write(self.cal.to_ical())
