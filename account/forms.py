from django import forms
from django.contrib.auth.models import User
from .models import Profile 

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)



class UsersRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirm_password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name','last_name', 'email', 'password') 
        
    def clean_confirm_password(self):
        cd = self.cleaned_data
        if cd['password'] != cd['confirm_password']:
            raise forms.ValidationError('Passord doesn\'t match.')
        return cd['confirm_password'] 


from .models import Profile 

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email') 

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo', 'program_level')