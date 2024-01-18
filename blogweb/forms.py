from django import forms
from . models import Blog
class fileupload(forms.ModelForm):
    class Meta:
        model= Blog
        fields='__all__'
        labels={
            'user_name':'your name',
            'review':'your review',
            'rating':'your rating'
        }
        error_messages = {
                'required': 'Please enter your name.',
                'max_length':'enter shorter name'
            
        }