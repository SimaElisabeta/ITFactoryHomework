from django.db import models

USER_GENDERS = [
    ("F", "Female"),
    ("M", "Male")
]


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=50, null=False)
    username = models.CharField(max_length=50, null=False)
    gender = models.CharField(max_length=1, choices=USER_GENDERS, null=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name} --- USERNAME: {self.username}'
