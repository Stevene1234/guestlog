from django.contrib import admin
from .models import Visit

@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ('name', 'visit_date', 'purpose', 'email', 'phone')
    search_fields = ('name', 'email', 'phone', 'purpose')
    list_filter = ('visit_date',)
