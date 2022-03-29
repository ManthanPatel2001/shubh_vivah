from django.contrib import admin
from .models import Customer,Intrest, Matched, Reject
# Register your models here.
admin.site.register(Customer)
admin.site.register(Intrest)
admin.site.register(Reject)
admin.site.register(Matched)

