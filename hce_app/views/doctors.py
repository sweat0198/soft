from django.shortcuts import render, redirect
from hce_app.decorators import allowed_to
from django.contrib import messages

from hce_app.models import CustomUser, Cure, Prescription


def doc_home(request):
    return render(request, 'Doctor/doc_home.html')


def doctor_interview(request):
    return render(request, 'Doctor/doctor_interview.html')


def med_result(request):
    return render(request, 'Doctor/med_result.html')


def prescrips(request):
    if request.method == 'POST':
        cure_number = request.POST['cure_number']
        user_id = request.POST['user_id']
        user = CustomUser.objects.get(id=user_id)
        prescription = Prescription.objects.create(user=user)
        prescription.save()
        for i in range(int(cure_number)):
            cure_name = request.POST['cure_name%s' % (i + 1)]
            cure_amount = request.POST['cure_amount%s' % (i + 1)]
            cure = Cure.objects.create(name=cure_name, daily_consume=cure_amount, prescription=prescription)
            cure.save()
        messages.success(request, "Successfully saved")
        return redirect('prescrips')

    users = CustomUser.objects.filter(authorize='normal', is_superuser=False)
    return render(request, 'Doctor/prescrips.html', context={'users': users})
