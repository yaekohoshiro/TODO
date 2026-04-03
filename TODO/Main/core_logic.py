from . import models
from django.db.models import Q, Count, QuerySet

def filter_task(progress = 0, tag = "my_tasks"):
    list_task = models.Task.objects.filter(Q(progress = progress) & Q(tag = tag))
    return list_task

def get_statistical(user: QuerySet):
    tasks = user.prefetch_related("task").get(id=2)
    counts = tasks.task.aggregate(
        count_0 = Count("progress", filter=Q(progress = 0)),
        count_1 = Count("progress", filter=Q(progress = 1)),
        count_2 = Count("progress", filter=Q(progress = 2)),
        count_3 = Count("progress", filter=Q(progress = 3)),
        count_4 = Count("progress", filter=Q(progress = 4)),
        )
    return counts
    '''
    list_task = models.Task.objects.filter(progress = progress)
    list_task = list_task.filter(tag = tag)
    return list_task
    '''