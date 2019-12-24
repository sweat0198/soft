from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.conf import settings

from hce_app.forms import EnterAnalysisResultForm
from hce_app.models import *
from hce_app.decorators import allowed_to


@allowed_to(auths=['normal', ])
def home(request):
    return render(request, 'Normal/home.html')


@allowed_to(auths=['normal', ])
def enter_result(request):
    if request.method == 'POST':
        form = EnterAnalysisResultForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data.pop('analysis_file')
            fs = FileSystemStorage()
            filename = fs.save(file.name, file)
            analysis_result = AnalysisResult.objects.create(user=request.user, report=filename,
                                                            report_name=filename)
            analysis_result.save()
            messages.success(request, message="Successfully added.", extra_tags='success')
        else:
            messages.error(request, message=form.errors, extra_tags='danger')
        return redirect('enter_result')
    return render(request, 'Normal/enter_result.html')


@allowed_to(auths=['normal', ])
def medical_hist(request):
    if request.method == 'POST':
        medical_history = request.POST['medical_history']
        user = request.user
        user.sickness = medical_history
        user.save()
        messages.success(request, message="Successfully changed.", extra_tags='success')
        redirect('medical_hist')
    return render(request, 'Normal/medical_hist.html')


@allowed_to(auths=['normal', ])
def prescriptions(request):
    prescriptions = request.user.taken_prescriptions.all()

    return render(request, 'Normal/prescriptions.html', context={'prescriptions': prescriptions})


@allowed_to(auths=['normal', ])
def user_interview(request):
    return render(request, 'Normal/user_interview.html')


@allowed_to(auths=['normal', ])
def test_over(request):
    return render(request, 'Normal/test_over.html')


@allowed_to(auths=['normal', ])
def online_test(request):
    return render(request, 'Normal/online_test.html')
