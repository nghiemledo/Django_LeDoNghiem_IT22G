from django.contrib import admin
from .models import BaiViet

# Register your models here.
class BaiVietAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']
    
admin.site.register(BaiViet, BaiVietAdmin)
