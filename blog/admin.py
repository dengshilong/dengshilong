from django.contrib import admin
# Register your models here.
from .models import Post,Category,Link,Page
from .forms import PostForm
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    form = PostForm
    list_display = ('title', 'publish_time')
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Link)
admin.site.register(Page)
