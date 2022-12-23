from django.shortcuts import render,redirect
from .models import Student,Proxy_Student
from .forms import StudentForm,Proxy_StudentForm
# Create your views here.
def home_page(request):
    return render(request,'base.html')

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

def Student_list(request):
    Student_list = Student.student_manager.all()
    return render(request,'myapp/student_list.html',{'student_list':Student_list})

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

def Student_proxy_list(request):
    proxy_student_list=Proxy_Student.proxy_manager.all()
    return render(request,'myapp/proxy_student_list.html',{'proxy_student_list':proxy_student_list})

def update_proxy_student(request, pk):
            selected_task = Proxy_Student.proxy_manager.get(roll_no=pk)
            if request.method=="POST":
                form = Proxy_StudentForm(request.POST, instance=selected_task)
                if form.is_valid():
                    form.save()
                    return redirect('student-proxy-list')
            else:
                form = Proxy_StudentForm(instance=selected_task)
            return render(request, 'myapp/update_proxy_task.html', {'form':form})
                                      
def delete(request,pk):
            task =  Proxy_Student.proxy_manager.get(roll_no=pk)
            if request.method == 'POST':
                task.delete()
                return redirect('student-proxy-list')
            return render(request,'myapp/delete_proxy_task.html',{'task':task})

