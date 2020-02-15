from django.urls import path
from . import views
from .views import ApplicantsApprovedView, ApplicantsSponsoredView, ApplicantsApprovedDetailView

urlpatterns = [

    # url for the application form
    path('applicationform/', views.application, name= 'application'),

    # url for the approved applicants- where sponsors can view approved applicants
    path('approvedapplicants/', ApplicantsApprovedView.as_view(), name= 'approvedlist'),

    # url for the sponsored applicants- where applicants can view if they're sponsored
    path('applicantssponsored/', ApplicantsSponsoredView.as_view(), name= 'applicantssponsored'),
    
    # url for the details of approved applicants
    path('applicantsapproveddetail/<int:pk>/', ApplicantsApprovedDetailView.as_view(), name= 'applicantdetail'),

]
