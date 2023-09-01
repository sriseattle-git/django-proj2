from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import CustomUser

# Extend Django's built-in UserCreationForm and UserChangeForm forms 
# so that they can use the new user model
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("email", "first_name", "last_name",)
        exclude = ("username",) # Didn't work to not show the username field in registration form...

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("email", "first_name", "last_name")