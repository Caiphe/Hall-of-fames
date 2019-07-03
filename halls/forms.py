from .models import Video
from django import forms

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = [ 'url', ]
        labels ={"url" : "YouTube Url"}


class SearchForm(forms.Form):
    search_term = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': "Search..."}), max_length=288)