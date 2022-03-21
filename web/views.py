from django.shortcuts import render, HttpResponse


def index(request):
    print('Hello')
    return HttpResponse('Hello')
