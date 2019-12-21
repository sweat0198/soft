from django.shortcuts import render
from HCE.decorators import allowed_to

from hce_app.models import CustomUser

def doc_home(request):
    return render(request, 'Doctor/doc_home.html')


def doctor_interview(request):
    return render(request, 'Doctor/doctor_interview.html')


def med_result(request):
    return render(request, 'Doctor/med_result.html')


def prescrips(request):
    users = CustomUser.objects.filter(authorize='normal')
    return render(request, 'Doctor/prescrips.html', context={'users':users})




