from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm
from .models import Profile
from .models import StudentModel
from .forms import StudentForm

def registration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        context = {
        'products': ['Товар 2', 'Товар 2', 'Товар 3'],
    }
        if form.is_valid():
            user = form.save()
            # сохранение номера
            Profile.objects.create(user=user, phone_number=form.cleaned_data.get('phone_number'))
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return render(request, 'homepage.html', context)
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
def index(request):
    context = {
        'products': ['Товар 2', 'Товар 2', 'Товар 3'],
    }
    return render(request, 'homepage.html', context)