from django import forms

class Members(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    paid = forms.FloatField()