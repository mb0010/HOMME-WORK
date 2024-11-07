from django import forms
from .models import User, Category, Vacancy

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'last_name', 'phone_number', 'email', 'username', 'location', 'profession', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ['category', 'title', 'description', 'location', 'phone_number_user', 'images']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }
