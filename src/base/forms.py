from django import forms
from .models import SavedPassword

class RegisterForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'inputEmail', 'placeholder': 'Username'}), label='Username', max_length=50)
	email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control', 'id': 'inputEmail', 'placeholder': 'Email'}), label='Email', max_length=255)
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'inputPassword', 'placeholder': 'Password'}), label='Password', max_length=255)
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'inputPassword', 'placeholder': 'Confirm Password'}), label='Confirm Password', max_length=255)

class PasswordForm(forms.ModelForm):
	class Meta:
		model = SavedPassword
		fields = '__all__'
		widgets = {
			'site': forms.TextInput(attrs={'class': 'form-control'}),
			'username': forms.TextInput(attrs={'class': 'form-control'}),
			'email': forms.EmailInput(attrs={'class': 'form-control'}),
			'password': forms.PasswordInput(attrs={'class': 'form-control', 'id': 'togglePass'})
		}