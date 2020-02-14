from django.contrib import admin
from .models import ApplicantInfo,ApprovedApplicant,SponsporsInfo

# Register your models here.

admin.site.register(ApplicantInfo)
admin.site.register(ApprovedApplicant)
admin.site.register(SponsporsInfo)
