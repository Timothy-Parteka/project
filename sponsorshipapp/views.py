from django.shortcuts import render

from django.http import HttpResponseRedirect

# imported the django generic views
from django.views.generic import ListView, DetailView

# imported ApplicantInfoForm from forms.py file
from .forms import ApplicantInfoForm

# imported models from models.py file
from .models import ApplicantInfo, ApprovedApplicant, SponsporsInfo

# Create your views here.


def application(request):

    context = {}

    form = ApplicantInfoForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
    
    context['form'] = form

    return render(request, 'application_form.html',context)

# ApplicantsApprovedView inherits ListView(generic views)
class ApplicantsApprovedView(ListView):
    # added the model to use
    model = ApprovedApplicant

    # added the template to use
    template_name = "applicants_approved_list.html"

    # added a context_object_name for our models
    context_object_name = "applicants_approved_list"


# ApplicantsSponsoredView inherits ListView(generic views)
class ApplicantsSponsoredView(ListView):
    # added the model to use
    model = SponsporsInfo

    # added the template to use
    template_name = "applicants_sponsored.html"

    # added a context_object_name for our models
    context_object_name = "applicants_sponsored_list"


# ApplicantsApprovedDetailView inherits DetailView(generic views)
class ApplicantsApprovedDetailView(DetailView):
    # added the model to use
    model = ApplicantInfo

    # added the template to use
    template_name = "approved_applicant_detail.html"
