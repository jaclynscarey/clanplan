from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile, Family, Attendee

class ExtendedUserCreationForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email',)




# class UserProfileForm(ExtendedUserCreationForm):
#     birthday = forms.DateField(required=True)



# class FamilyForm(forms.ModelForm):
#     name = forms.CharField(required=True)
#     family_code = forms.CharField(required=True)


# class AttendeeForm(forms.ModelForm):
#     pass