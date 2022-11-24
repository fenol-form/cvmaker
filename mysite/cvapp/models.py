from django.db import models
from django.urls import reverse

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

    def get_absolute_url(self):
        return reverse("cvs")
