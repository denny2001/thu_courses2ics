class Course(object):
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.section = kwargs.get('section')  # a tuple of (weekday, order) e.g. (3, 5) stands for '3-5'
        self.lecturer = kwargs.get('lecturer')  # lecturer name
        self.location = kwargs.get('location')  # course location

        self.start_week = kwargs.get('start_week')
        self.end_week = kwargs.get('end_week')

        self.week_span = kwargs.get('week_span')  # a tuple of start and end weeks

    def __repr__(self):
        return '  '.join(
            [f'{self.section[0]}-{self.section[1]}', self.name, self.lecturer, self.location,
             str(self.week_span)])

    def __eq__(self, other):
        return self.name == other.name and self.lecturer == other.lecturer and self.location == other.location
