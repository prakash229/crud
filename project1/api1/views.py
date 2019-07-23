from django.shortcuts import render, render_to_response
from rest_framework import generics
from .serializers import todolistSerializer
from .models import todolist

# Create your views here.
class CreateView(generics.ListAPIView):
    queryset=todolist.objects.all()
    serializer_class = todolistSerializer

    def perform_create(self, serializer):
        serializer.save()

def index(request):
    objlist = todolist.objects.all()
    fulllist = {
        "listnumber" : objlist
    }
    return render(request,'api1t/basic.html', fulllist)


def taskdelete(request):
    some_var = request.POST.getlist('checks')
    print(some_var)
    for i in some_var:
        todolist.objects.filter(id=i).delete()

    objlist = todolist.objects.all()
    fulllist = {
        "listnumber" : objlist
    }
    return render(request,'api1t/basic.html', fulllist)

def taskdone(request):
    some_var = request.POST.getlist('checks')
    print(some_var)
    for i in some_var:
        todolist.objects.filter(id=i).update(taskstatus=True)

    objlist = todolist.objects.all()
    fulllist = {
        "listnumber" : objlist
    }
    return render(request,'api1t/basic.html', fulllist)


def addnewtask(request):
    task=request.POST.get("newtask","")
    #print(task)
    if task != "":
        t = todolist(taskdetails=task)
        t.save()
    return render(request,'api1t/addtask.html')

def searchpage(request):
    return render (request,'api1t/search.html')

def searchtask(request):
    choice=request.POST.get("checks","")
    inp=request.POST.get("searchinput")
    #print(task)

    kwargs = {
        '{0}'.format(choice): inp
        }

    objlist = todolist.objects.filter(**kwargs)
    fulllist = {
        "listnumber" : objlist
    }
    return render(request,'api1t/basic.html',fulllist)
