from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    subject = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    message = forms.CharField()


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)


class RegisterUserForm(forms.Form):
    username = forms.CharField(max_length=100)
    id_number = forms.CharField(max_length=100)
    birth_date = forms.DateTimeField(required=True)
    password = forms.CharField(max_length=100)
    gender = forms.ChoiceField(choices=[('male', 'male'), ('female', 'female'), ])
    email = forms.EmailField(max_length=100)
    authorize = forms.ChoiceField(choices=(('normal', 'normal'), ('doctor', 'doctor')))
    sickness = forms.CharField(max_length=100, required=False, empty_value=True)
    file = forms.FileField(required=False)


class EnterAnalysisResultForm(forms.Form):
    analysis = forms.ChoiceField(
        choices=(('blood', 'Blood Analysis'), ('urine', 'Urine Analysis'), ('others', 'Others')))
    analysis_file = forms.FileField()
