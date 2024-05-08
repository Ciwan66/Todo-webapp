from django import forms
from .models import Team
from accounts.models import CustomUser

class TeamForm(forms.ModelForm):

    class Meta:
        model = Team
        fields = [
            'name','description'
        ]

class AddMemberForm(forms.ModelForm):

    class Meta:
        model = Team
        fields = ['members']