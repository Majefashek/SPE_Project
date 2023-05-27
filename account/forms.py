from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import CustomUser
from django import forms
from django.contrib.auth.forms import PasswordChangeForm

class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput)
    new_password1 = forms.CharField(widget=forms.PasswordInput)
    new_password2 = forms.CharField(widget=forms.PasswordInput)

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields[:-1]

class RegisterUserForm(CustomUserCreationForm):
	class Meta:
		model = CustomUser
		fields = UserCreationForm.Meta.fields + ( 'profile_image',)
		

	def __init__(self, *args, **kwargs):
		super(RegisterUserForm, self).__init__(*args, **kwargs)
		for field in self.fields.values():
			field.widget.attrs['class'] = 'form-control'


class Edit_userForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username','age', 'profile_image', 'bio' )

