from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    test1=request.session.get('test1')
    if not test1:
        request.session['test1']='ali'
    print(request.session.get('test1'))
    request.session.pop('test1')
    print(request.session.get('test1'))
    return HttpResponse('Website index')