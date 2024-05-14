from django.forms import ModelForm
from products.models import Review
from django import forms

class AddReviewForm(ModelForm):
    class Meta:
        model=Review
        fields=['comment','star_given']

class DeleteReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [] 