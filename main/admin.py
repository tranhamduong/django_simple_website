from django.contrib import admin
from .models import Candidate


# Register your models here.

@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    readonly_fields  = ["jackpot_keys"]