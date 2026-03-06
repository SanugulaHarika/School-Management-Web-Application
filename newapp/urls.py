from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("student/",views.student,name="student"),
    path('teacher/',views.home,name='teachers'),
    path('add-teachers/',views.add_teacher,name="addteacher"),
    path('update_teacher/<str:id>',views.update_teacher,name="update"),
    path('delete/<str:id>',views.delete_teacher,name="delete"),
    path('add_student/',views.add_student,name="addstudent"),
    path('update_student/<str:id>',views.update_student,name="updatestudent"),
    path('delete_student/<str:id>',views.delete_student,name="deletestudent")
]