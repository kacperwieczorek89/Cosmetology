from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


def pass_length_validation(value):
    if len(value)<8:
        raise ValidationError("Password is too short")


class UserCreationForm(forms.ModelForm):
    pass_1 = forms.CharField(widget=forms.PasswordInput(), validators=[pass_length_validation])
    pass_2 = forms.CharField(widget=forms.PasswordInput(), validators=[pass_length_validation])

    class Meta:
        model = User
        fields = [
            'username',
            'pass_1',
            'pass_2',
        ]

    def clean(self):
        data = super().clean()
        if data.get('pass_1') != data.get('pass_2'):
            raise ValidationError("Passwords are not the same")
        return data


class UserPermissionForm(forms.ModelForm):
    class Meta:

        model = User
        fields = ['user_permissions']
        widgets = {
            'user_permissions': forms.CheckboxSelectMultiple
        }



