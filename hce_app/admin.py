from django.contrib import admin
from .models import *

admin.site.register(CustomUser)
admin.site.register(Doctor)
admin.site.register(TestResult)
admin.site.register(AnalysisResult)
admin.site.register(Cure)
admin.site.register(Prescription)
# Register your models here.

admin.site.site_header = "Health Care in Everywhere "
admin.site.site_title = "HCE Admin"
