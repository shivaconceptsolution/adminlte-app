from django.db import models

class Category(models.Model):
    catname=models.CharField(max_length=50)
    def __str__(self):
        return str(self.catname)