from django.db import models

class Data(models.Model):
    int=models.IntegerField()
    char=models.CharField(max_length=200)
    text=models.TextField()
    date=models.DateField()

class Uploadfile(models.Model):
    file=models.FileField(upload_to="files")

class Users(models.Model):
    user_type_choices=[('customer','Customer'),('employee','Employee')]
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    type=models.CharField(max_length=200,choices=user_type_choices,default='customer')

class Files(models.Model):
    company=models.CharField(max_length=200)
    version=models.CharField(max_length=200)
    file=models.FileField()

    def __str__(self):
        return self.company+" "+self.version

    class Meta:
        unique_together = (("company","version"),)
