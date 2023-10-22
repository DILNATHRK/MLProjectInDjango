from django.urls import path
from medicalapp import views

urlpatterns = [
    path('', views.home, name="home"),
    path('predict/', views.predict, name="predict"),
    path('result/', views.result, name="result"),
    path('recordData/', views.recordData, name="recordData"),
]
