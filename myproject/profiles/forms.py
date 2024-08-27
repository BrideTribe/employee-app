from django import forms
from .models import Profile
from users.models import CustomUser



class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'phone']
        
