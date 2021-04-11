from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Widgets
from django.db.models import Sum


# Create your views here.

def index(request):
    widgets = Widgets.objects.all()
    sum= Widgets.objects.aggregate(Sum('quantity'))
    print(sum)
    return render(request, 'index.html', {'widgets': widgets, 'sum': sum})

def submit(request):
    print(request)
    Widgets.objects.create(
        description=request.POST['description'],
        quantity=request.POST['quantity'],
    )
    return redirect('/')

def delete(request, w_id):
    w= Widgets.objects.get(id=w_id)
    w.delete()
    return redirect('/')


