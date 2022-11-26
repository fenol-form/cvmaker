from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class CV(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField()
    city = models.CharField(max_length=20)
    post = models.CharField(max_length=100)
    experience = models.IntegerField()  # work experience for month
    education = models.TextField(blank=True)
    key_skills = models.TextField(blank=True)
    languages = models.TextField(blank=True)

    username = models.ForeignKey(
        User,
        #on_delete=models.PROTECT()
        on_delete=models.CASCADE
    )

    def get_absolute_url(self):
        return reverse("cvs")

    def __str__(self):
        return f"{self.first_name} {self.last_name}\n" \
               f"{self.age}\n" \
               f"{self.city}\n" \
               f"{self.post}\n" \
               f"{self.experience}\n" \
               f"{self.education}\n" \
               f"{self.key_skills}\n" \
               f"{self.languages}\n";
