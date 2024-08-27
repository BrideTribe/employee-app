from django.db import models
from django.contrib.auth.models import User
# from users.models import CustomUser
from myproject import settings
from PIL import Image


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE )
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    phone = models.CharField(default= '080-', max_length=11)
    site_name = models.CharField(default='EagleWings', max_length=225)
    
    def __str__(self):
        return f'{self.image} {self.user.first_name} Profile'
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
