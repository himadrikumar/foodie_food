from django import forms

from .models import FoodRequest


class RatingForm(forms.ModelForm):
    class Meta:
        model = FoodRequest
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
