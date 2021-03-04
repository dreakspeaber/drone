from django import forms





class LoginForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control','placeholder':'username'}))
    password = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={'class' : 'form-control','placeholder':'password'})) 
    

