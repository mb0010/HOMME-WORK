from django.shortcuts import render, redirect
from .models import User, Category, Vacancy
from .forms import UserForm, VacancyForm


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') 
    else:
        form = UserForm()
    return render(request, 'register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username, password=password)
            request.session['user_id'] = user.id  
            return redirect('home')
        except User.DoesNotExist:
            return render(request, 'login.html', {'error': 'Номи корбар ё гузарвожа нодуруст аст'})
    return render(request, 'login.html')


def home(request):
    if 'user_id' not in request.session:
        return redirect('login')  
    return render(request, 'home.html')  


def create_vacancy(request):
    if 'user_id' not in request.session:
        return redirect('login')
    if request.method == 'POST':
        form = VacancyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  
    else:
        form = VacancyForm()
    return render(request, 'create_vacancy.html', {'form': form})


def view_vacancies_by_category(request):
    if 'user_id' not in request.session:
        return redirect('login')
    
    categories = Category.objects.all() 
    
    if request.method == 'POST':
        category_id = request.POST.get('category')  
        selected_category = Category.objects.get(id=category_id)  
        
    
        vacancies = Vacancy.objects.filter(category=selected_category)
        
        return render(request, 'vacancy_list.html', {
            'vacancies': vacancies,
            'category': selected_category
        })

    return render(request, 'select_category.html', {'categories': categories})