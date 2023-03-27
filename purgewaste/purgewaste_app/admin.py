from django.contrib import admin
from .models import Waste ,Invoice,InvoiceItem


admin.site.register(Waste)
admin.site.register(Invoice)
admin.site.register(InvoiceItem)
