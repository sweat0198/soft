from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    authorize = models.CharField(max_length=255, default='normal')  # normal, doctor, admin
    gender = models.CharField(max_length=255, default='male')  # male, female
    id_number = models.CharField(max_length=255, null=True)
    birth_date = models.DateTimeField(null=True)
    sickness = models.CharField(max_length=255, null=True)

    @property
    def spam_true(self):
        return self.is_active


class Doctor(models.Model):
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE, related_name='doctor_user')
    total_vote = models.IntegerField(default=0)
    vote_number = models.IntegerField(default=0)
    licence_file = models.FileField(upload_to='upload/', null=True)

    @property
    def avg_vote(self):
        return self.total_vote / self.vote_number

    def __str__(self):
        return "{}: {}".format(self.__class__.__name__, self.user.username)


class TestResult(models.Model):
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE, related_name='test_owner')
    sickness = models.CharField(max_length=255)
    accuracy = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)

    @property
    def give_accuracy(self):
        return self.accuracy / 100


class AnalysisResult(models.Model):
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE, related_name='analysis_owner')
    report = models.FileField()
    report_name = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)


class Prescription(models.Model):
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE, related_name='prescription_owner')
    created_date = models.DateTimeField(auto_now_add=True)


class Cure(models.Model):
    name = models.CharField(max_length=255)
    daily_consume = models.IntegerField(default=0)
    prescription = models.ForeignKey('Prescription', on_delete=models.CASCADE, related_name='prescription')
