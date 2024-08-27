from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.forms import UserUpdateForm, UserRegisterForm
from users.models import CustomUser
# from django.contrib.auth.models import User


# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = UserRegisterForm
    form = UserUpdateForm
    
    model = CustomUser
    list_display = (
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "is_active",
    )
    list_filter = (
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "is_active",
    )
    fieldsets = (
        (None, {"fields": (
            "first_name",
            "last_name",
            "email",
            "password" )}
        ),
        ("permissions", {"fields": (
            "is_staff",
            "is_active",
            "groups",
            "user_permissions" )}
        ),
    )
    add_fieldsets = (
        (None, {"fields": (
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
            "is_staff",
            "is_active",
            "groups",
            "user_permissions" )}
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)

#Register the models so that it shows up on the admin page.
admin.site.register(CustomUser, CustomUserAdmin)