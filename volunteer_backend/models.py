from django.db import models


class User(models.Model):
    id = model.IntegerField(primary_key=True, auto_now_add=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    location = models.IntegerField()

    def __str__(self):
        return self.id;