from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from hce_app.models import *
from hce_app.decorators import allowed_to
from hce_app.forms import *


def index(request):
    if request.user.is_authenticated:
        user = request.user
        if user.authorize == 'normal':
            return redirect('home')
        elif user.authorize == 'doctor':
            return redirect('doc_home')
        else:
            return redirect('admin_url')
    return render(request, 'commons/index.html')


def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(**form.cleaned_data)
            if user:
                login(request, user)
                return redirect('index')
            else:
                messages.add_message(request, level=messages.ERROR, message="Username or password is wrong",
                                     extra_tags='danger')
                return redirect('login')
        else:
            messages.warning(request, "Username or password is not filled decently")
            print("Username or password is not filled decently")
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('index')
        return render(request, 'commons/login.html')


def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data.pop('file')
            user = CustomUser.objects.create_user(**form.cleaned_data)

            if user.authorize == 'doctor':
                file = request.FILES['file']
                fs = FileSystemStorage()
                filename = fs.save(file.name, file)
                doctor = Doctor.objects.create(user=user, licence_file=filename)
                doctor.save()
            login(request, user)
            return redirect('index')
        else:
            messages.add_message(request, level=messages.ERROR, message="Some fields are wrong",
                                 extra_tags='danger')
            redirect('register_user')
    return render(request, 'commons/registration_user.html')


def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print("Name: {name}\nSubject: {subject}\nEmail: {email}\nMessage: {message}".format(**form.cleaned_data))
        else:
            print("Geçemedi")
    return render(request, 'commons/contact-us.html')


def logout_view(request):
    logout(request)
    return redirect('index')
