from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser, Profile

# Create profile model 
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = "Profile"

# Tell the admin panel to use these forms by extending from UserAdmin
# add_form and form: specify the forms to add and change user instances
# fieldsets: specify the fields to be used in editing users
# add_fieldsets: specify fields to be used when creating a user (via the admin panel??)
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    model = CustomUser

    # Remove username from list_display, fieldsets, add_fieldsets
    # since CustomUser has indicated username = None 
    # Add first_name & last_name to list_display, fieldsets, add_fieldsets
    # list_display: defines fields and order of display for list of users view
    # fieldsets: defines field groupings and order in change user form
    # add_fieldsets: defines field groupings and order in add new user form
    
    list_display = (
#        "username",
        "email",
        "first_name",
        "last_name",        
        "is_active",
        "is_staff",
        "is_superuser",
        "last_login",
    )
    list_filter = ("is_active", "is_staff", "is_superuser")
    fieldsets = (
        (None, {"fields": ("first_name", "last_name", "email", "password")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_staff",
                    "is_active",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
#                    "username",
                    "email",             
                    "password1",
                    "password2",
                    "first_name",
                    "last_name",                       
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)
    inlines = (ProfileInline,) # Show profile in admin UX

# Register profile as part of admin UX
admin.site.register(Profile)


