from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'main/datatables.net.html')

def about(request):
    return render(request, 'main/about.html')
def calendar(request):
    return render(request, 'main/calendar.html')