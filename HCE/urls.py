"""HCE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view, name='home')
Including another URLconf
    1. Import the include function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from hce_app.views import normals, commons, doctors

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # commons
    path('', commons.index, name='index'),
    path('login/', commons.login_page, name='login'),
    path('logout/', commons.logout_view, name='logout'),
    path('register_user/', commons.register_user, name='register_user'),
    path('contact/', commons.contact_us, name='contact_us'),

    # normal user
    path('home/', normals.home, name='home'),
    path('enter_result/', normals.enter_result, name='enter_result'),
    path('medical_hist/', normals.medical_hist, name='medical_hist'),

    path('prescriptions/', normals.prescriptions, name='prescriptions'),
    path('test_over/', normals.test_over, name='test_over'),
    path('user_interview/', normals.user_interview, name='user_interview'),

    # doctors
    path('doc_home/', doctors.doc_home, name='doc_home'),
    path('doctor_interview/', doctors.doctor_interview, name='doctor_interview'),
    path('med_result/', doctors.med_result, name='med_result'),
    path('prescrips/', doctors.prescrips, name='prescrips'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
