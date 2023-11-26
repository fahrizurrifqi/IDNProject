from django.contrib import admin
from .models import *
from .forms import *
# Register your models here.

@admin.register(Training,Permintaan,PurchaseOrder,Penawaran,Invoice)

class viewAdmin(admin.ModelAdmin):
    pass
