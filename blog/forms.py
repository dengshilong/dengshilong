from pagedown.widgets import AdminPagedownWidget
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    content = forms.CharField(widget=AdminPagedownWidget())

    class Meta:
        model = Post
        fields = "__all__"
