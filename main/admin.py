from django.contrib import admin

from .models import *

admin.site.register(Product)
admin.site.register(Article)
admin.site.register(Tag)
admin.site.register(Profile)
admin.site.register(Vote)
