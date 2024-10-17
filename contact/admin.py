from django.contrib import admin
from .models import CollaborateRequest

# Register the CollaborateRequest model
@admin.register(CollaborateRequest)
class CollaborateRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','message', 'is_read', 'created_on')
    list_filter = ('is_read',)
    