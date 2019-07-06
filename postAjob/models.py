from django.db import models

class joblist(models.Model):
    job_title = models.CharField(max_length=250)
    company_name = models.CharField(max_length=500)
    issu_date = models.CharField(max_length=50)
    company_logo =models.CharField(max_length=1000)

class job(models.Model):
    no_of_job = models.ForeignKey(joblist,on_delete=models.CASCADE)
    job_type = models.CharField(max_length=100)
