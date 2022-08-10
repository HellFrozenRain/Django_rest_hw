from django.db import models
from Usersapp.models import MyUser

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=128, unique=True)
    repository_url = models.URLField(blank=True)
    users = models.ManyToManyField(MyUser)

    class Meta:
        ordering = ['pk']

    def __str__(self):
        return f'{self.name}'


class Note(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['pk']