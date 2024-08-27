from django import forms
from . import models


class CreatePost(forms.ModelForm):
    class Meta:
        model = models.Worksite
        fields = ['site_name','title','content','slug','absentees']
        
        
class UpdatePost(forms.ModelForm):
    class Meta:
        model = models.Worksite
        fields = ['title','content','absentees']


class DeletePost():
    pass