from django import forms
from .models import *

# class DateInput(forms.DateInput):
    # input_type = 'date'


class BlogForm(forms.ModelForm):
	body = forms.CharField(widget=forms.Textarea(attrs={'rows': '10', 'style': 'resize: none;'}))
	# pub_date = forms.CharField(widget=DateInput())
	class Meta:
		model = Blog
		exclude = 'user',

