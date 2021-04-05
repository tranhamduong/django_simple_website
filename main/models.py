from django.db import models
import random
from django.core.validators import RegexValidator
from django.forms import ModelForm

# Create your models here.
class Candidate(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=200, blank=False)
    phone_number = models.CharField(max_length=10, blank=False, validators=[RegexValidator(regex='\+?(0|84)\d{9}', message='Sai định dạng số điện thoại', code='invalid_phone_number' )])
    # image = StdImageField(upload_to='image', variations={'thumbnail': {'width': 300, 'height': 300}}, null=True, blank=True)
    image = models.URLField(max_length = 1500)

    def get_random_number():
        return random.randrange(1000,9999)
    jackpot_keys = models.CharField(max_length=4, default= get_random_number, unique=True, editable=False)
    
    
    
    def __str__(self):
        return '%s' % (self.full_name)
    
