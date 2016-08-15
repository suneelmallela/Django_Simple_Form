from django import forms

class testform(forms.Form):
    vmid = forms.CharField(max_length=32)
    vmstate = forms.CharField(max_length=10)
