from wsgiref.simple_server import demo_app
from django.shortcuts import render

# Create your views here.
def default(request):
    context = {"data":"Home Page of Django App"}
    return render(request,'api/default.html', context)

