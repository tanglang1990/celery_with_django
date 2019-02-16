import time
from celery.task import Task


class CourseTask(Task):
    name = 'course-task'

    def run(self, *args, **kwargs):
        print('start course task')
        print('args={}, kwargs={}'.format(args, kwargs))
        time.sleep(4)
        print('end course task')
