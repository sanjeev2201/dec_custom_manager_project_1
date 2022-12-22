from django.urls import path
from .  import views
urlpatterns = [
    path('student/', views.Student_index,name='student'),
    path('student_proxy/',views.Student_proxy_index,name='student-proxy')
]
