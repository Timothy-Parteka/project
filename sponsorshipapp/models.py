from django.db import models
from django.urls import reverse


# created models for the applicants and added fields
# for taking in their information
class ApplicantInfo(models.Model):
    first_name = models.CharField(max_length=252)
    last_name = models.CharField(max_length=252)
    phone_number = models.CharField(max_length=252, unique=True)
    email_address = models.EmailField(max_length=128, unique=True)

    # upload_to='documents/' - This where our files will be uploaded to i.e 
    # a folder named documents
    birth_certificate = models.FileField(upload_to='documents/')
    national_id = models.FileField(upload_to='documents/')
    school_name = models.CharField(max_length=252)
    address = models.CharField(max_length=252)
    academic_level = models.CharField(max_length=100)
    year_of_completion = models.CharField(max_length=100)
    reason_to_be_sponsored = models.TextField(max_length=1000)
    recomendation_letter = models.FileField(upload_to='documents/')

    # return the applicants email address
    def __str__(self):
        return self.email_address

    def get_absolute_url(self):
        return reverse('applicantdetail', args=[str(self.id)])


# models for approving successful applicants, which is performed
# by the staff
class ApprovedApplicant(models.Model):

    # performs a many to one relationship
    applicant_info = models.ForeignKey(ApplicantInfo, on_delete= models.CASCADE)
    approved = models.CharField(max_length=100)

    def __str__(self):
        return self.approved


# models for the sponsors information and a ForeignKey
# for the applicants they wish to sponsors
class SponsporsInfo(models.Model):
    first_name = models.CharField(max_length=252)
    last_name = models.CharField(max_length=252)
    email_address = models.EmailField(max_length=252, unique=True)
    occupation = models.CharField(max_length=100)
    sponsored_applicant = models.ForeignKey(ApplicantInfo, on_delete= models.CASCADE)

    def __str__(self):
        return self.email_address
