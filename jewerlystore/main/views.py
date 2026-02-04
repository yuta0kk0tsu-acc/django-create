from django.shortcuts import render

# Главная страница
def home(request):
    return render(request, 'main/index.html')

# Страница каталога
def catalog(request):
    return render(request, 'main/catalog.html')

# Страница "О нас"
def about(request):
    return render(request, 'main/about.html')