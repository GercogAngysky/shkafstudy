from django.contrib import admin

from .models import *

class PostAdmin(admin.ModelAdmin):
	model = Post
	list_display = [f.name for f in Post._meta.get_fields()]
	search_fields = ("title", )


admin.site.register(Post, PostAdmin)