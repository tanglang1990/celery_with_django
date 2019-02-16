from datetime import timedelta

import djcelery

djcelery.setup_loader()

CELERY_QUEUES = {
    'beat_tasks': {
        'exchange': 'beat_tasks',
        'exchange_tye': 'direct',
        'binding_key': 'beat_tasks'
    },
    'work_queue': {
        'exchange': 'work_queue',
        'exchange_tye': 'direct',
        'binding_key': 'work_queue'
    }

}

CELERY_DEFAULT_QUEUE = 'work_queue'

CELERY_IMPORTS = (
    'course.tasks',
)

# 有些情况下可以防止死锁
CELERY_FORCE_EXECV = True

# 设置并发的worker数量
CELERY_CONCURRENCY = 4

# 允许重试
CELERY_ACKS_LATE = True

# 每个worker最多执行100个任务被消费，可以防止内存泄漏
CELERYD_MAX_TASKS_PER_CHILD = 100

# 单个任务的最大执行时间
CELERYD_TASK_TIME_LIMIT = 12 * 30

# 启动消息队列命令
# python manage.py celery worker -l INFO


# 定时任务
CELERYBEAT_SCHEDULE = {
    'task1': {
        'task': 'course-task',
        'schedule': timedelta(seconds=5),
        'options': {
            'queue': 'beat_tasks'
        }
    }
}

# 启动定时任务命令
# python manage.py celery beat -l INFO


# 监控工具
# pip install celery

# celery flower --broker
# 此外在django中可以通过：
# python manage.py celery flower
# python manage.py celery flower --basic_auth=ten:ten

# 然后访问 http://localhost:5555/