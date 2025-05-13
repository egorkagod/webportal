from django.db import models

from root.models import Profile


class Resume(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='resumes')
    about = models.TextField()
    profession = models.CharField(max_length=100)
    education = models.CharField(max_length=100)
    skills = models.TextField()
    portfolio = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)