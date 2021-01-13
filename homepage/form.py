
from django.forms import ModelForm
from .models import  scholarship
from django import forms
from .models import application_table


class DateInput(forms.DateInput):
    input_type = 'date'

class add_scholarship_form(forms.ModelForm):



    class Meta:
        model = scholarship
        fields = ['title', 'applicants', 'short_description','long_description','img','boy','girl','both','active','document','fromdate','toomdate','scholarship_form']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'special'}),
            'fromdate': DateInput(),
            'toomdate': DateInput(),
        }

        labels = {
            'title': 'Title',
            'applicants': 'Applicants',
            'short_description': 'Short_description',
            'img': 'Picture',
            'both': ' Total(boys and girls)per branch',
            'boy': 'Boys per branch(if distributed in boys and girls)',
            'girl': 'Girls per branch(if distributed in boys and girls)',
            'fromdate': 'Starting date',
            'toomdate': 'End date',
        }


class extra_documents_form(forms.ModelForm):
    class Meta:
        model = application_table
        fields = ['applied_extra1','applied_extra2', 'applied_scholarship_form']
        labels = {
            'applied_scholarship_form':'Application form(Only in pdf)',
            'applied_extra1': 'Other Document 1',
            'applied_extra2': 'Other Document 2',

        }