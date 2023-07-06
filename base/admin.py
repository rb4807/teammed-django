from django.contrib import admin

from .models import Departments,Doctor,Booking

# Register your models here.

admin.site.register(Departments)
admin.site.register(Doctor)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'number', 'doc', 'booked', 'date')

admin.site.register(Booking, BookingAdmin)

