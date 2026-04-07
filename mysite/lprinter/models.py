from django.db import models

class Duties (models.Model):
    name = models.CharField(verbose_name="Pareigos")

    def __str__(self):
        return self.name


class Worker(models.Model):
    first_name = models.CharField(verbose_name="Vardas")
    last_name = models.CharField(verbose_name="Pavarde")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class  Work(models.Model):
    task = models.CharField(verbose_name="Užduotis")
    worker = models.ForeignKey(to="Worker", on_delete=models.SET_NULL, null=True, blank=True)
    duties = models.ManyToManyField(to="Duties", verbose_name="Pareigos")

    def __str__(self):
        return self.task


class Product(models.Model):
    work = models.ForeignKey(to="Work", verbose_name="Darbuotojas", on_delete=models.SET_NULL, null=True, blank=True)
    order = models.DateField(verbose_name="Paslauga", null=True, blank=True)

    LOAN_STATUS = (
        ('p', 'Priskirtas'),
        ('i', 'Įvykdytas'),
        ('l', 'Laisvas'),
    )

    status = models.CharField(verbose_name='Statusas_darbu', max_length=1, choices=LOAN_STATUS, blank=True, default='l')
