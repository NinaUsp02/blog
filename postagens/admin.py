from django.contrib import admin

from .models import Postagem, List, Comment

admin.site.register(Postagem)
admin.site.register(List)
admin.site.register(Comment)
