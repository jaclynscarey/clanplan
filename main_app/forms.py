from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile, Family, Attendee

class ExtendedUserCreationForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email',)

class UserProfileForm(ExtendedUserCreationForm):
    birthday = forms.DateField(required=True)

    class Meta(ExtendedUserCreationForm.Meta):
        model = User
        fields = ExtendedUserCreationForm.Meta.fields + ('birthday',)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()

            birthday = self.cleaned_data['birthday']
            user_profile = UserProfile(user=user, birthday=birthday)
            user_profile.save()

            # Additional logic to link user to Family and create Attendee if needed

        return user



# class FamilyForm(forms.ModelForm):
#     name = forms.CharField(required=True)
#     family_code = forms.CharField(required=True)


# class AttendeeForm(forms.ModelForm):
#     pass