from django import forms

class Log(forms.Form):
    user = forms.CharField(label='Usuario', initial='admin', max_length=25,
        widget=forms.TextInput(attrs={"placeholder" : "Usuario" }))
    password = forms.CharField(
        label='Contraseña', max_length=32, widget=forms.PasswordInput) 
