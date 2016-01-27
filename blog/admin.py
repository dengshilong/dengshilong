from django.contrib import admin
# Register your models here.
from .models import Post,Tag,Category,Link,Page
from .forms import PostForm
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    form = PostForm
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Link)
admin.site.register(Page)
