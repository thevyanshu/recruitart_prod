from django.forms import ModelForm, NumberInput, Textarea, TextInput, EmailInput, CheckboxInput, FileInput
from app1.models import Application


class ApplicationForm(ModelForm):
    
    class Meta:
        model = Application
        fields = ['current_designation', 'current_location', 'preferred_designation', 'preferred_location', 'current_salary', 'expected_salary', 'can_join', 'name', 'mobile_no', 'alternate_mobile', 'total_experience', 'email', 'pg_name', 'ug_name', 'message', 'resume', 'agree']
        widgets = {
            'current_designation': TextInput(attrs={'class': 'form-control'}),
            'current_location': TextInput(attrs={'class': 'form-control'}),
            'preferred_location':TextInput(attrs={'class': 'form-control'}),
            'preferred_designation': TextInput(attrs={'class': 'form-control'}),
            'current_salary': NumberInput(attrs={'class': 'form-control'}),
            'expected_salary': NumberInput(attrs={'class': 'form-control'}),
            'can_join': TextInput(attrs={'class': 'form-control'}),
            'name': TextInput(attrs={'class': 'form-control'}),
            'mobile_no': NumberInput(attrs={'class': 'form-control'}),
            'alternate_mobile': NumberInput(attrs={'class': 'form-control'}),
            'total_experience': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'}),
            'pg_name': TextInput(attrs={'class': 'form-control'}),
            'ug_name': TextInput(attrs={'class': 'form-control'}),
            'message': Textarea(attrs={'class': 'form-control'}),
            'resume': FileInput(attrs={'class': 'form-control'}),
            'agree': CheckboxInput(attrs={'class': 'form-check-input'}),
        }
