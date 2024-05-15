from django.forms import ModelForm
from products.models import Review
from django import forms

class AddReviewForm(ModelForm):
    class Meta:
        model=Review
        fields=['comment','star_given']

class UpdateReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['star_given','comment']
