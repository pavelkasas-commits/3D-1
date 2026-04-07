from django.contrib import admin
from .models import Duties, Worker, Work, Product

# Register your models here.


admin.site.register(Duties)
admin.site.register(Worker)
admin.site.register(Work)
admin.site.register(Product)