from django.contrib import admin

from .models import Market, Vendor, Product
admin.site.register(Market)
admin.site.register(Vendor)
admin.site.register(Product)

