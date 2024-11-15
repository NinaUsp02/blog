from django.contrib import admin

from .models import Postagem, Comment, Category

admin.site.register(Postagem)
admin.site.register(Comment)
admin.site.register(Category)
