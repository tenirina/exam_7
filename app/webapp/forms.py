from django import forms
from django.forms import widgets


class RecordForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label="Name")
    email = forms.CharField(max_length=100, required=True, label="Email")
    text = forms.CharField(max_length=1500, required=True, label="Description", widget=widgets.Textarea)


class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Search", initial='')
