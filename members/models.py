from django.db import models

# Create your models here.

class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    date_of_joining = models.DateField(null=True)

    def __str__(self):
        return f"{self.lastname} , {self.firstname} - {self.phone}"
