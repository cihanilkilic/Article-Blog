from django.contrib.auth.models import User
from django import forms


class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-Control',
        'placeholder':'Kullanıcı-Adı'

    }))
    password=forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-Control',
        'placeholder':'Şifre'

    }))








class RegisterForm(forms.Form):
    first_name=forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-Control',
        'placeholder':'Adınız'

    }))

    last_name=forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-Control',
        'placeholder':'Soyadınız'

    }))
    username=forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-Control',
        'placeholder':'Kullanıcı-Adınız'

    }))
    email=forms.CharField(widget=forms.EmailInput(attrs={
        'class':'form-Control',
        'placeholder':'E mail Adresi'

    }))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-Control',
        'placeholder':'Şifre'

    }))
    password2=forms.CharField(
        widget=forms.PasswordInput(attrs={
        'class':'form-Control',
        'placeholder':'Şifre Tekrar'

    }))


#class kısmı register için
    class Meta:
        model=User
        fields=['first_name','last_name','username','password','email','password1','password2',]