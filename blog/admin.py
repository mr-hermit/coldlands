from django.contrib import admin
from blog.models import Post, Category, Tag

class PostAdmin(admin.ModelAdmin):
    exclude = ['posted']
    prepopulated_fields = {'postid': ('title',)}
    
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'catid': ('name',)}
    
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)