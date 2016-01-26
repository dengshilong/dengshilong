from django.contrib import admin
# Register your models here.
from .models import Post,Tag,Category,Link
from .forms import PostForm
class PostAdmin(admin.ModelAdmin):
    form = PostForm
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Link)
