from django.db import models

# Create your models here.

#company model here
class CompanyModel(models.Model):
    name=models.CharField(max_length=50)
    location=models.CharField(max_length=50) 
    about=models.TextField()
    type=models.CharField(max_length=100,choices=
                            (('IT','IT'),
                             ('Non IT','Non IT'),
                             ('Phone Mobile','Phone Mobile')
                             ))
    added_date=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)
    def __str__(self):
        return self.name

#Employee Model 

