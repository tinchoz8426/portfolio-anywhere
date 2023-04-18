from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label=False, widget= forms.TextInput(attrs={"class": "form-control", "placeholder":"Nombre"}), required=True)
    email = forms.EmailField(widget= forms.EmailInput(attrs={"class": "form-control", "placeholder":"Correo"}), required=True)
    message = forms.CharField(widget= forms.Textarea(attrs={"class": "form-control", "placeholder": "Mensaje", "style":"height: 200px;"}), required=True)