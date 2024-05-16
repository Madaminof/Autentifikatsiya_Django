from django.forms import ModelForm
from products.models import Review
from django import forms

from users.models import CustomUser


class AddReviewForm(ModelForm):
    class Meta:
        model=Review
        fields=['comment','star_given']

class UpdateReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['star_given','comment']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username','first_name','last_name','email','password']
