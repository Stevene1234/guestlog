from django import forms
from .models import Visit


class VisitForm(forms.ModelForm):
    class Meta:
        model = Visit
        fields = ['name', 'email', 'phone', 'purpose']
        widgets = {
            'visit_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
