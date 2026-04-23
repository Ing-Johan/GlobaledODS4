from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistroForm(UserCreationForm):
    edad = forms.IntegerField(
        min_value=5, max_value=120,
        widget=forms.NumberInput(attrs={
            'placeholder': 'Edad',
            'class': 'form-input'
        })
    )

    class Meta:
        model  = User
        fields = ['username', 'password1', 'password2', 'edad']
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Usuario',
                'class': 'form-input'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'placeholder': 'Contraseña', 'class': 'form-input'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirmar contraseña', 'class': 'form-input'})

    def save(self, commit=True):
        user = super().save(commit)
        perfil = user.perfil  # creado por señal
        perfil.edad = self.cleaned_data['edad']
        perfil.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Usuario', 'class': 'form-input'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña', 'class': 'form-input'})
    )


class RecuperarForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Usuario o correo electrónico',
            'class': 'form-input'
        })
    )