from django.forms import ModelForm
from .models import Candidate
from django import forms
from django.core.validators import RegexValidator

class CandidateForm(ModelForm):
    class Meta:
        model = Candidate
        fields=['full_name', 'phone_number', 'image']   
        
class LookupForm(forms.Form):
    lookup = forms.CharField(label='Phone number:', max_length=15, validators=[RegexValidator(regex='\+?(0|84)\d{9}', message='Sai định dạng số điện thoại', code='invalid_phone_number' )])
    
class JackpotForm(forms.Form):
    lookup = forms.CharField(label='Your phone number:', max_length=15, validators=[RegexValidator(regex='\+?(0|84)\d{9}', message='Sai định dạng số điện thoại', code='invalid_phone_number' )])
    jackpot = forms.CharField(label='Your ticket number: ', max_length=4)
    
