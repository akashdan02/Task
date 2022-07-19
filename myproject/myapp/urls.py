from django.contrib import admin
from django.urls import path
from .views import Student_lists, student_detail, StudentAPIView,StudentDetails


urlpatterns = [
    # path('student/', Student_lists),
    path('student/', StudentAPIView.as_view()),
    path('detail/<int:pk>/', student_detail)
    # path('detail/<int:id>/', StudentDetails.as_view())
]
