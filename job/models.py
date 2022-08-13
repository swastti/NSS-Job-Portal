from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class StudentUser(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    mobile=models.CharField(max_length=15,null=True)
    image=models.FileField(null=True)
    gender=models.CharField(max_length=10,null=True)
    type=models.CharField(max_length=15,null=True)
    # address=models.CharField(max_length=150,null=True)
    def _str_(self):
        return self.user.username

class Recruiter(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    mobile=models.CharField(max_length=15,null=True)
    image=models.FileField(null=True)
    company=models.CharField(max_length=150,null=True)
    gender=models.CharField(max_length=10,null=True)
    type=models.CharField(max_length=15,null=True)
    status=models.CharField(max_length=20,null=True)

    def _str_(self):
        return self.user.username

    # is_private = request.POST.get('is_private', False);

class Job(models.Model):
    recruiter = models.ForeignKey(Recruiter,on_delete=models.CASCADE)
    start_date=models.DateField()
    end_date=models.DateField()
    title=models.CharField(max_length=150)
    salary=models.FloatField(max_length=30)
    image=models.FileField()
    description=models.CharField(max_length=350,null=True)
    experience=models.CharField(max_length=50)
    location=models.CharField(max_length=120)
    skills=models.CharField(max_length=120)
    creationdate=models.DateField()

    def _str_(self):
        return self.title

class JobD(models.Model):
    recruiter = models.ForeignKey(Recruiter,on_delete=models.CASCADE)
    start_date=models.DateField()
    end_date=models.DateField()
    title=models.CharField(max_length=150)
    salary=models.FloatField(max_length=30)
    image=models.FileField()
    description=models.CharField(max_length=350,null=True)
    experience=models.CharField(max_length=50)
    location=models.CharField(max_length=120)
    skills=models.CharField(max_length=120)
    creationdate=models.DateField()

    def _str_(self):
        return self.title

class Apply(models.Model):
    job = models.ForeignKey(Job,on_delete=models.CASCADE)
    student = models.ForeignKey(StudentUser,on_delete=models.CASCADE)
    applydate=models.DateField()
    def _str_(self):
        return self.id