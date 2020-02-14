from django import forms
from .models import ApplicantInfo



class ApplicantInfoForm(forms.ModelForm):

    class Meta:
        model = ApplicantInfo
        fields = "__all__"
