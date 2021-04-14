from django import forms
from .models import Feedback

class FeedbacksForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('name', 'email', 'text',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control border'}),
            'email': forms.EmailInput(attrs={'class': 'form-control border'}),
            'text': forms.Textarea(attrs={'class': 'form-control border'})
        }

