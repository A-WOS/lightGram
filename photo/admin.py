from django.contrib import admin
from photo.models import Photo


# class PhotoAdmin(admin.ModelAdmin):
#     list_display = ('author', 'text')


admin.site.register(Photo)
