from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class UserRegisterForm(UserCreationForm):
    
    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "email", "password", "is_staff", "is_active", "groups", "user_permissions"]
        
class UserUpdateForm(UserChangeForm):
     
    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "email", "password", "is_staff", "is_active", "groups", "user_permissions"]
 

        