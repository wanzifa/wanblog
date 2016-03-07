from django import forms
from wanzi.models import Post, Tag

class Search(forms.ModelForm):
    index = forms.CharField(max_length=128)

