from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Sandelis(models.Model):
    pavadinimas = models.CharField()
    vieta = models.CharField(blank=True, null=True)
    aprasymas = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Sandelis"
        verbose_name_plural = "Sandelis"


    def __str__(self):
        return self.pavadinimas



class Filamentai(models.Model):
        Miedziagos = (
            ("PLA","PLA"),
            ("PETG", "PETG"),
            ("ABS","ABS"),
            ("TPU", "TPU"),
            ("Nezinoma", "Nezinoma"),


        )

        Spalvos = (
            ("Raudona","Raudona"),
            ("Geltona","Geltona"),
            ("Juoda","Juoda"),
            ("Balta","Balta"),
            ("Nezinoma","Nezinoma"),

        )

        statusas =(
        ("Priimta","Priimta"),
        )



        uzsakymas = models.CharField()
        medziaga = models.CharField(choices=Miedziagos, blank=True, null=True)
        spalva = models.CharField(choices=Spalvos, blank=True, null=True)
        tiekiejas = models.CharField(blank=True, null=True,)
        status = models.CharField(choices=statusas, blank=True, null=True,)

        atvaziavo_kg = models.FloatField(blank=True, null=True,)
        sunaudota_kg = models.FloatField(default=0)
        kaina = models.DecimalField(max_digits=1000, decimal_places=2)

        sandelis = models.ForeignKey(Sandelis, on_delete=models.CASCADE, related_name="filamentai")






        def likutis(self):
                return self.atvaziavo_kg - self.sanaudota_kg

        def __str__(self):
                return f"{self.uzsakymas} ({self.medziaga}, {self.spalva})"


        class Meta:
            verbose_name = "Filamentai"
            verbose_name_plural = "Filamentai"





class Task(models.Model):
    title = models.CharField(verbose_name="Uzduotis")
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="tasks",null=True,blank=True,)
    creat_at = models.DateTimeField(default=timezone.now, editable=False)
    content = models.TextField(blank=True, null=True)

    STATUS_CHOICES = [
        ("u","Uzregistruota"),
        ("P","Patvirtinta"),
        ("A","Atlikta"),
        ("a","Atsaukta"), ]

    status = models.CharField(choices=STATUS_CHOICES, default='')

    def __str__(self):
        return self.title


