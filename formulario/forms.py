from django import forms

class ContactoForm(forms.Form):
    nombre = forms.CharField(label='nombre', max_length=100)
    email = forms.EmailField()
    mensaje = forms.CharField(widget=forms.Textarea)