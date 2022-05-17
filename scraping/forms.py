from django import forms

from scraping.models import City, Symptom


class FindForm(forms.Form):
    city = forms.ModelChoiceField(
        queryset=City.objects.all(),
        to_field_name='slug',
        required=False,
        widget=forms.Select(
            attrs={
                'class': 'form-control'}))
    symptom = forms.ModelChoiceField(
        queryset=Symptom.objects.all(),
        to_field_name='slug',
        required=False,
        widget=forms.Select(
            attrs={
                'class': 'form-control'}))
