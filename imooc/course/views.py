from django.http import JsonResponse
from django.shortcuts import render

from .tasks import CourseTask


def do(request):
    print('start request')
    CourseTask.delay()
    print('end request, start response')
    return JsonResponse({'result': 'ok'})
