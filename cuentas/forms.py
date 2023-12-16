from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from ckeditor.fields import RichTextFormField


class FormularioRegistroUsuario(UserCreationForm):
    username = forms.CharField(label='Nombre de usuario')
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)
        
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {key: '' for key in fields} 
  
        
class FormularioEditarPerfil(UserChangeForm):
    password = None
    email = forms.EmailField(label='Cambiar email', required=False)
    first_name = forms.CharField(label='Cambiar nombre', required=False)
    last_name = forms.CharField(label='Cambiar apellido', required=False)
    biografia = RichTextFormField()
    avatar = forms.ImageField(required=False)
        
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'biografia', 'avatar']


      
