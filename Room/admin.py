from django.contrib import admin
# from Room.views import bookings
from .models import *

# Register your models here.
admin.site.register(Register)
admin.site.register(State)
admin.site.register(District)
admin.site.register(Owner_Detail)
admin.site.register(Image)
admin.site.register(Status)
admin.site.register(bookings)