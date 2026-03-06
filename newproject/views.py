from django.shortcuts import render

def index(request):
    return render(request,"index.html")

def student(request):
    return render(request,"student.html")