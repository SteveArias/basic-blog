from django.contrib import admin
from .models import BlogAuthor, BlogPost, BlogComment

admin.site.register(BlogAuthor)
admin.site.register(BlogPost)
admin.site.register(BlogComment)