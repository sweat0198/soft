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
    if request.method == 'POST':
        ache = request.POST['ache']
        pain = request.POST['pain']
        erythema = request.POST['erythema']
        inflamed = request.POST['inflamed']
        nausea = request.POST['nausea']
        hair_lose = request.POST['hair_lose']
        appetite = request.POST['appetite']
        weakness = request.POST['weakness']
        insomnia = request.POST['insomnia']
        nosebleed = request.POST['nosebleed']
        dizziness = request.POST['dizziness']
        fever = request.POST['fever']
        other = request.POST['other']

        diseases = {'Sniffle': 0, 'Sinusitis': 0, 'diarrhea': 0, 'Fungal Inflammation': 0, 'Anemia': 0}

        diseases['Sniffle'] += 0.1 if ache == 'head' else 0
        diseases['Sniffle'] += 0.05 if fever == 'yes' else 0
        diseases['Sniffle'] += 0.1 if ache == 'throat' else 0
        diseases['Sniffle'] += 0.1 if weakness == 'yes' else 0
        diseases['Sniffle'] += 0.05 if insomnia == 'yes' else 0
        diseases['Sniffle'] += 0.1 if other == 'cough' else 0
        diseases['Sniffle'] += 0.1 if other == 'tear' else 0
        diseases['Sniffle'] += 0.1 if other == 'sneeze' else 0
        diseases['Sniffle'] += 0.1 if other == 'runny_nose' else 0

        diseases['Sinusitis'] += 0.15 if ache == 'head' else 0
        diseases['Sinusitis'] += 0.1 if weakness == 'yes' else 0
        diseases['Sinusitis'] += 0.1 if other == 'cough' else 0
        diseases['Sinusitis'] += 0.15 if other == 'runny_nose' else 0
        diseases['Sinusitis'] += 0.15 if nausea == 'yes' else 0
        diseases['Sinusitis'] += 0.1 if dizziness == 'yes' else 0

        diseases['diarrhea'] += 0.1 if ache == 'stomach_ache' else 0
        diseases['diarrhea'] += 0.15 if pain == 'stomach_pain' else 0
        diseases['diarrhea'] += 0.15 if nausea == 'yes' else 0
        diseases['diarrhea'] += 0.15 if fever == 'yes' else 0
        diseases['diarrhea'] += 0.1 if weakness == 'yes' else 0
        diseases['diarrhea'] += 0.1 if other == 'fluid_loss' else 0

        diseases['Fungal Inflammation'] += 0.6 if ache == 'no' else 0
        diseases['Fungal Inflammation'] += 0.15 if weakness == 'yes' else 0
        diseases['Fungal Inflammation'] += 0.1 if hair_lose == 'yes' else 0
        diseases['Fungal Inflammation'] += 0.1 if fever == 'yes' else 0
        diseases['Fungal Inflammation'] += 0.05 if insomnia == 'yes' else 0

        diseases['Anemia'] += 0.2 if hair_lose == 'yes' else 0
        diseases['Anemia'] += 0.3 if weakness == 'yes' else 0
        diseases['Anemia'] += 0.15 if dizziness == 'yes' else 0
        diseases['Anemia'] += 0.1 if ache == 'head' else 0

        print(diseases)
        sorted_diseases_as_list = [k for k, v in sorted(diseases.items(), key= lambda item: item[1])]
        print(sorted_diseases_as_list)
        max_probable_disease = sorted_diseases_as_list[-1]
        max_probable_disease_ratio = diseases[max_probable_disease]

        if max_probable_disease_ratio >= 0.6:
            messages.success(request, message="You have %{} {}.".format(max_probable_disease_ratio*100,max_probable_disease), extra_tags='success')
        else:
            messages.error(request, message="Your sickness not determined.", extra_tags='danger')

    return render(request, 'Normal/online_test2.html')
