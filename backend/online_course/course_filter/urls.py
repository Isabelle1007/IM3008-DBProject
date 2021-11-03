from django.urls import path
from course_filter import views

urlpatterns = [
    path('search/quick', views.quick_search)
]