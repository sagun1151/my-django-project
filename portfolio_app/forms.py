from django import forms
from .models import Project
from .models import Portfolio

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description']

class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['title', 'contact_email', 'is_active', 'about']