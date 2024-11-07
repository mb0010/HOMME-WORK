from django.db import models

from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)  
    name = models.CharField(max_length=100) 
    last_name = models.CharField(max_length=100) 
    phone_number = models.CharField(max_length=15, unique=True)  
    email = models.EmailField(max_length=255, unique=True)  
    username = models.CharField(max_length=150, unique=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    profession = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=128)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} {self.last_name}"


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='vacancies')
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=100, blank=True, null=True)
    phone_number_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='vacancies')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    images = models.ImageField(upload_to='vacancy_images/', blank=True, null=True)  

    def __str__(self):
        return self.title