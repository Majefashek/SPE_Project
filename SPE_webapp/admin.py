from django.contrib import admin

from .models import Post, CustomUser, Jobs, Comments

admin.site.register(Post)
admin.site.register(CustomUser)
admin.site.register(Jobs)
admin.site.register(Comments)
