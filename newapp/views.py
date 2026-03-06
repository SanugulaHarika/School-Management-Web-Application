from django.shortcuts import render,redirect
from .models import Teacher,Students
from django.contrib import messages


# Create your views here.

def home(request):
    teachers = Teacher.objects.all()
    return render(request,"index.html",{"allteachers":teachers})

def student(request):
    students = Students.objects.all()
    return render(request,"student.html",{"allstudents":students})    

def add_teacher(request):
    if request.method == "POST":
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        image = request.FILES.get('image')

        teacher = Teacher(
            name = name,
            subject = subject,
            contact = contact,
            email = email,
            image = image if image else None
        )
        teacher.save()
        return redirect("home")
    return render(request,"index.html")

def update_teacher(request,id):
    if request.method == "POST":
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        image = request.FILES.get('image')
    
        teacher = Teacher(
            id = id,
            name = name,
            subject = subject,
            contact = contact,
            email = email,
            image = image if image else None
        )
        teacher.save()
        return redirect("home")
    return render(request,"index.html",{'teacher':teacher})

def delete_teacher(request,id):
    teacher = Teacher.objects.filter(id=id)
    teacher.delete()

    return redirect("home")

def add_student(request):
    if request.method == "POST":
        name = request.POST.get('name')
        rollno = request.POST.get('rollno')
        DOB = request.POST.get('DOB')
        contact = request.POST.get('contact')
        image = request.FILES.get('image')

        student = Students(
            name = name,
            rollno = rollno,
            DOB = DOB,
            contact = contact,
            image = image if image else None
        )
        student.save()
        return redirect("student")
    return render(request,"student.html")

def update_student(request,id):
    if request.method == "POST":
        name = request.POST.get('name')
        rollno = request.POST.get('rollno')
        DOB = request.POST.get('DOB')
        contact = request.POST.get('contact')
        image = request.FILES.get('image')
    
        student = Students(
            id = id,
            name = name,
            rollno = rollno,
            DOB = DOB,
            contact = contact,
            image = image if image else None
        )
        student.save()
        return redirect("student")
    return render(request,"student.html",{'student':student})

def delete_student(request,id):
    student = Students.objects.filter(id=id)
    student.delete()

    return redirect("student")