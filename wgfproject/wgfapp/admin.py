from django.contrib import admin
from .models import *

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":('title',)}


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":('title',)}


admin.site.register(Member)
admin.site.register(Prayer)
admin.site.register(Testimony)
admin.site.register(Post, PostAdmin)
admin.site.register(Event)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment)

