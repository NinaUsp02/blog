from django.contrib import admin

from .models import Postagem, Review, List

admin.site.register(Postagem)
admin.site.register(Review)
admin.site.register(List)