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

class NewFamilyForm(ExtendedUserCreationForm):
    birthday = forms.DateField(required=True)
    family_name = forms.CharField(required=True)
    family_code = forms.CharField(required=True)

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

            # logic to create Attendee
            attendee = Attendee(user=user)
            attendee.save()
            
            # Logic to create Family
            name = self.cleaned_data['family_name']
            family_code = self.cleaned_data['family_code']
            family = Family(name=name, family_code=family_code, admin=user)
            family.save()
            user_profile.family = family
            user_profile.save()

        return user

class JoinFamilyForm(ExtendedUserCreationForm):
    birthday = forms.DateField(required=True)
    # family_name = forms.CharField(required=True)
    family_code = forms.CharField(required=True)

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

            # logic to create Attendee
            attendee = Attendee(user=user)
            attendee.save()
            
            # Logic to join existing Family
            # family_name = self.cleaned_data['family_name']
            family_code = self.cleaned_data['family_code']
            family = Family.objects.get(family_code=family_code)
            user_profile.family = family
            user_profile.save()
            


            # name = self.cleaned_data['family_name']
            # family_code = self.cleaned_data['family_code']
            # family = Family(name=name, family_code=family_code, admin=user)
            # family.save()
            # user_profile.family = family
            # user_profile.save()

        return user