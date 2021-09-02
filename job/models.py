from django.db import models

# Create your models here.


'''
django model field:
    -html widget
    -validation
    -db size

'''
JOB_TYPE = (
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
)

class job(models.Model):   ##TABLE
    title= models.CharField(max_length=100)   ###column
    #location
    job_type = models.CharField(max_length=15 , choices=JOB_TYPE)
    describtion = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    #category 
    experience = models.IntegerField(default=1)

    def __str__(self):
        return self.title