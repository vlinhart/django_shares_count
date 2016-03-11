from django.contrib import admin

from shares_count.models import Share

class ShareAdmin(admin.ModelAdmin):
    list_display = ('created', 'modified', 'shares', 'content_object')


admin.site.register(Share, ShareAdmin)
