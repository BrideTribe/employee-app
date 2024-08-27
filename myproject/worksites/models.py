from django.db import models
from users.models import CustomUser
from django.urls import reverse

# Create your models here.
class Worksite(models.Model):
    site_name = models.CharField(max_length=100)
    title = models.CharField(max_length=75)
    content = models.TextField()
    slug = models.SlugField()
    absentees = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=None)
    
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("worksite-detail", kwargs={"pk": self.pk})
    