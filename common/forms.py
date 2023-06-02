from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile
# class UserForm(UserCreationForm):
#     email = forms.EmailField(label="이메일")
#     school = forms.CharField(max_length=200, label="학교이름", required=True)
#     class Meta():
#         model = User
#         fields = ("school", "first_name", "last_name", "username", "password1", "password2", "email")


class UserForm(UserCreationForm):
    email = forms.EmailField(label="email")
    school_name = forms.CharField(
        max_length=200, label="school_name", required=True)

    class Meta():
        model = User
        fields = ("school_name", "first_name", "last_name", "username", "password1", "password2", "email")

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            instance = Profile.objects.create(
                user=user, school_name=self.cleaned_data['school_name'])
            instance.save()
        return user


class SchoolForm(forms.Form):
    school_name = forms.CharField(max_length=200)

# from django import forms
# from django.contrib.auth.forms import UserCreationForm
