from django import forms
from .models import CV, Education, Experience, Skill

class CVForm(forms.ModelForm):
    class Meta:
        model = CV
        fields = ['full_name', 'email', 'phone', 'address', 'summary']


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['school', 'degree', 'start_year', 'end_year']

    def clean_degree(self) -> str:
        degree = self.cleaned_data['degree']
        if len(degree) < 3:
            raise forms.ValidationError('Degree name too short')
        return degree

    def clean_school(self) -> str:
        school = self.cleaned_data['school']
        if any(char.isdigit() for char in school):
            raise forms.ValidationError('School name can not contain digits')
        return school

    def clean(self):
        cleaned_data = super().clean()
        start = cleaned_data.get('start_year')
        end = cleaned_data.get('end_year')
        if start and end and end < start:
            raise forms.ValidationError('Start year must be before end year')

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['company', 'position', 'start_date', 'end_date', 'description']

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name']
