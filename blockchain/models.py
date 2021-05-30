from django.db import models

class Token(models.Model):
    uid = models.CharField(max_length=200)
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=400)
    img = models.URLField(max_length=500)
    created = models.DateField(auto_now_add=True)


    def __str__(self):
        return f'{self.uid} - Token'