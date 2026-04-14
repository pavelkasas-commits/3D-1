from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Task(models.Model):
    title = models.CharField(verbose_name="Užduotis")
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="tasks",null=True,blank=True,)
    creat_at = models.DateTimeField(default=timezone.now, editable=False)
    content = models.TextField(blank=True, null=True)

    STATUS_CHOICES = [
        ("u","Užregistruota"),
        ("P","Patvirtinta"),
        ("A","Atliktas"),
        ("a","Atšaukta"), ]

    status = models.CharField(choices=STATUS_CHOICES, default='')

    def __str__(self):
        return self.title


# class Sandelis(models.Model):
#     pavadinimas = models.CharFIeld
#







