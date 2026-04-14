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


class Sandelis(models.Model):
    pavadinimas = models.CharField()
    vieta = models.CharField(blank=True, null=True)
    aprasymas = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.pavadinimas



class Filamentai(models.Model):
        Miedziagos = (
            ("PLA","PLA"),
            ("PETG", "PETG"),
            ("ABS","ABS"),
            ("TPU", "TPU"),

        )

        pavadinimas = models.CharField()
        medziaga = models.CharField(choices=Miedziagos, blank=True, null=True)
        spalva = models.CharField()
        tiekiejas = models.CharField(blank=True, null=True,)

        atvaziavo_kg = models.FloatField(blank=True, null=True,)
        sunaudota_kg = models.FloatField(default=0)
        kaina = models.DecimalField(max_digits=1000, decimal_places=2)

        sandelis = models.ForeignKey(Sandelis, on_delete=models.CASCADE, related_name="filamentai")

        verbose_name = "Filamentai"
        verbose_name_plural = "Filamentai"

        def likutis(self):
                return self.atvaziavo_kg - self.sanaudota_kg

        def __str__(self):
                return f"{self.pavadinimas} ({self.medziaga}, {self.spalva})"









