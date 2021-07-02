from django.contrib import admin

from post.models import Post


class PostAdmin(admin.ModelAdmin):
    search_fields = ['author', 'content']
    list_display = ('author', 'content')


admin.site.register(Post, PostAdmin)
