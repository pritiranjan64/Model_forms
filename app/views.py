from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse

def insert_topic(request):
    ETFO=TopicForm()
    d={'ETFO':ETFO}
    if request.method=='POST':
        TFDO=TopicForm(request.POST)
        if TFDO.is_valid():
            TFDO.save()
            return HttpResponse('insert is done')
        else:
            return HttpResponse('invalid')
    return render(request,'insert_topic.html',d)


def insert_webpage(request):
    EWFO=WebpageForm()
    d={'EWFO':EWFO}
    if request.method=='POST':
        WDFO=WebpageForm(request.POST)
        if WDFO.is_valid():
            WDFO.save()
            return HttpResponse('insert is done')
        else:
            return HttpResponse('invalid')
    return render(request,'insert_webpage.html',d)


def insert_access(request):
    EAFO=AccessRecordForm()
    d={'EAFO':EAFO}
    if request.method=='POST':
        ADFO=AccessRecordForm(request.POST)
        if ADFO.is_valid():
            ADFO.save()
            return HttpResponse('insert is done')
        else:
            return HttpResponse('invalid')
    return render(request,'insert_access.html',d)