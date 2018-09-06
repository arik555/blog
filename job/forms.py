from django import forms
from .models import *
from django.contrib import auth

class JobForm(forms.ModelForm):
	img = forms.ImageField(label='Image')
	summary = forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'style': 'resize: none;'}))
	class Meta:
		model = Job
		exclude = 'user',

class UserRegisterForm(auth.forms.UserCreationForm):
	password2 = forms.CharField(widget=forms.PasswordInput, help_text='Use exactly as above. Case Sensitive.', label='Confirm Password')
	password1 = forms.CharField(widget=forms.PasswordInput, help_text='Use a strong password.', label='Password')
	class Meta:
		model = auth.models.User
		fields = ('first_name','last_name','username','email','password1','password2',)

	def clean(self):
		password2 = self.cleaned_data.get('password2')
		password1 = self.cleaned_data.get('password2')
		if password1 != password2:
			raise forms.ValidationError('Passwords Mismatch!')
		return self.cleaned_data


class UserLoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)


class UserEditForm(auth.forms.UserChangeForm):

	class Meta:
		model = auth.models.User
		fields = ('first_name','last_name','email','password',)

