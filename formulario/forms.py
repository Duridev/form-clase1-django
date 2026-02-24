from django import forms

class COntactoForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    email = forms.EmailField()
    mensaje = forms.CharField(widget=forms.Textarea)