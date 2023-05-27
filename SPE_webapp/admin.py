from django.contrib import admin

from .models import Post, CustomUser, Jobs, Comments,likes

admin.site.register(Post)

admin.site.register(Jobs)
admin.site.register(Comments)
admin.site.register(likes)
