from django.contrib import admin
from .models import Contact

# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'address', 'profession', 'tel_number')
    search_fields = ('name', 'email', 'profession')
    list_filter = ('profession',)