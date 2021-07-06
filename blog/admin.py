from blog.models import Blog, BlogPics
from django.contrib import admin

admin.site.site_header = "Welcome to blogging panel"
admin.site.site_title = "Manage Blogs"

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','slug', 'description')
    list_display_links = ('title',)
    list_filter = ('description',)


class PicAdmin(admin.ModelAdmin):
    list_display = ('image',)

admin.site.register(BlogPics,PicAdmin)
admin.site.register(Blog, BlogAdmin)