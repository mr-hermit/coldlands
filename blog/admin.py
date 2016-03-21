from django.contrib import admin

from blog.models import Post,Tag

# class TagInline(admin.TabularInline):
#     model = Post.tags.through

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # inlines = [TagInline]
    search_fields = ['tag']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass