# forms.py
from django import forms
from .models import Message
from crispy_forms.bootstrap import *
from crispy_forms.helper import FormHelper

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3}),
        }
