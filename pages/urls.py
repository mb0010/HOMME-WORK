from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('', views.home, name='home'),
    path('create_vacancy/', views.create_vacancy, name='create_vacancy'),
    path('view_vacancies_by_category/', views.view_vacancies_by_category, name='view_vacancies_by_category'),
]
