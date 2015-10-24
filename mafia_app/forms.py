from django import forms
from mafia_app.models import *

from django.core.exceptions import ValidationError
from django.core.validators import *

class addPhaseForm(forms.Form):
    reddit_url = forms.URLField(label='Reddit comment url', validators=[
        RegexValidator('reddit\.com/\S+/comments/[A-Za-z0-9]{6}/',
            message="That dosen't seem to be a comment thread",
            code="Invalid url"
        ),
    ])
    phase_type = forms.ChoiceField(label='Phase', choices=Phase._meta.get_field('phaseType').choices)
    phase_number = forms.IntegerField(label='Day')
