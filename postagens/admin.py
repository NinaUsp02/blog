from django.contrib import admin

from .models import Postagem, List, Comment, Category

admin.site.register(Postagem)
admin.site.register(List)
admin.site.register(Comment)
admin.site.register(Category)
