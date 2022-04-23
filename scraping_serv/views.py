from django.shortcuts import render
import datetime


def home(request):
    date = datetime.datetime.now().date()
    name = 'Bebra'
    cont = {'date': date, 'name': name}
    return render(request, 'home.html',cont)
