from django.urls import path
from .  import views
urlpatterns = [
    path('home/',views.home_page,name='home'),
    path('student/', views.Student_index,name='student'),
    path('student-list/',views.Student_list,name='student-list'),
    path('student_proxy/',views.Student_proxy_index,name='student-proxy'),
    path('student-proxy-list/',views.Student_proxy_list,name='student-proxy-list'),
    path('edit_proxy/<int:pk>', views.update_proxy_student,name='update-proxy-student'),
    path('delete_proxy/<int:pk>', views.delete,name='delete-proxy-student'),
]
