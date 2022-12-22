from django.shortcuts import render
from .models import Student,Proxy_Student
from .forms import StudentForm,Proxy_StudentForm
# Create your views here.

def Student_index(request):
    Student_list = Student.student_manager.all()
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'myapp/student_list.html',{'student_list':Student_list})
    else:
        form = StudentForm()
    return render(request,'myapp/create_student.html',{'form':form})
def Student_proxy_index(request):
    proxy_student_list=Proxy_Student.proxy_manager.all()
    if request.method=='POST':
        form=Proxy_StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'myapp/proxy_student_list.html',{'proxy_student_list':proxy_student_list})
    else:
        form=Proxy_StudentForm()
    return render(request,'myapp/create_proxy_student.html',{'form':form})