from django.db import models

# Create your models here.

class File(models.Model):
    title = models.CharField(max_length=100, null=True)
    discription = models.CharField(max_length=3000, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    file_source_path = models.CharField(max_length=100, null=True)


    def __str__(self):
        return f"{self.name}   {self.date_created}"