from django.contrib import admin

from .models import Post,CustomUser,Jobs,comments

admin.site.register(Post)
admin.site.register(CustomUser)
admin.site.register(Jobs)
admin.site.register(comments)
