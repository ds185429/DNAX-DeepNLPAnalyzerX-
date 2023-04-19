from django.db import models

# Create your models here.
class Users(models.Model):
    user_type_choices=[('customer','Customer'),('employee','Employee')]
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    type=models.CharField(max_length=200,choices=user_type_choices,default='customer')

class ConfigFiles(models.Model):
    file_name=models.CharField(max_length=200)
    file=models.FileField(upload_to="ConfigFiles")

    def __str__(self):
        return self.file_name

    class Meta:
        unique_together = (("file_name"),)

# class ConfigFiles(models.Model):
#     file_name=models.CharField(max_length=200)
#     file=models.FileField(upload_to="ConfigFiles")
#
#     def __str__(self):
#         return self.file_name
#
#     class Meta:
#         unique_together = (("file_name"),)
