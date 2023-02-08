from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import CustomUser


class RegisterUserForm(UserCreationForm):
	class Meta:
		model = CustomUser
		fields = UserCreationForm.Meta.fields + ('age', 'avatar', 'bio', 'is_admin',)

	def __init__(self, *args, **kwargs):
		super(RegisterUserForm, self).__init__(*args, **kwargs)
		for field in self.fields.values():
			field.widget.attrs['class'] = 'form-control'




class Edit_userForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email')

