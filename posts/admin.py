from django.contrib import admin
from .models import Post, Category

class PostAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
