from django import forms
from django.contrib.auth.models import User, Group
from django.utils.translation import gettext_lazy as _

from apps.profile.models import Profile


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email',)

    def __init__(self, request, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for arr in self.fields:
            if arr == "first_name" or arr == "last_name":
                self.fields[arr].widget.attrs.update(
                    {'class': 'form-control ',
                     'required': 'required',
                     }, )
            else:
                self.fields[arr].widget.attrs.update(
                    {'class': 'form-control ', 'required': 'required'}, )


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        groups = forms.ModelChoiceField(queryset=Group.objects.all(),
                                        required=True)
        fields = ('groups',)

    def __init__(self, request, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        self.fields['groups'].widget.attrs = {'class': 'select2 select2-multiple'}


class ProfileForm(forms.ModelForm):
    profile_image = forms.ImageField(label=_('Profil Resmi'), required=False,
                                     error_messages={'invalid': _("Image files only")}, widget=forms.FileInput)

    class Meta:
        model = Profile
        fields = (
            'tc',
            'birthday',
            'profile_image',
        )

    def __init__(self, request, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        for arr in self.fields:
            if arr == "birthday":
                self.fields[arr].widget.attrs = {'class': 'form-control ', 'autocomplete': 'off',
                                                 'id': 'kt_datepicker_1', 'placeholder': 'gg.aa.yyyy',
                                                 'data-date-format': 'dd.mm.yyyy', }
            elif arr == "tc":
                self.fields[arr].widget.attrs = {'class': 'form-control ',
                                                 'oninput': 'javascript: if (this.value.length > 11) this.value = this.value.slice(0, 11)'}
            elif arr == "profile_image":
                self.fields[arr].widget.attrs = {'class': 'dropify form-control w-56 block mx-auto',
                                                 'style': 'display:none;'}
            else:
                self.fields[arr].widget.attrs.update(
                    {'class': 'select2-search__field ', 'placeholder': 'Cinsiyet', 'required': 'true'})


class ContactForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phoneNumber',)

    def __init__(self, request, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for arr in self.fields:
            self.fields[arr].widget.attrs.update({'class': 'select2-search__field '})


class UserUpload(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email',)

    def __init__(self, request, *args, **kwargs):
        super(UserUpload, self).__init__(*args, **kwargs)
        for arr in self.fields:
            self.fields[arr].widget.attrs.update(
                {'class': 'form-control ', 'required': 'required'}, )


class ProfileUpload(forms.ModelForm):
    profile_image = forms.ImageField(label=_('Profil Resmi'), required=False,
                                     error_messages={'invalid': _("Image files only")}, widget=forms.FileInput)

    class Meta:
        model = Profile
        fields = (
            'tc',
            'birthday',
            'profile_image',
        )

    def __init__(self, request, *args, **kwargs):
        super(ProfileUpload, self).__init__(*args, **kwargs)
        for arr in self.fields:
            if arr == "birthday":
                self.fields[arr].widget.attrs = {'class': 'form-control ', 'autocomplete': 'off',
                                                 'id': 'kt_datepicker_1', 'placeholder': 'gg.aa.yyyy',
                                                 'data-date-format': 'dd.mm.yyyy', }
            elif arr == "tc":
                self.fields[arr].widget.attrs = {'class': 'form-control ',
                                                 'oninput': 'javascript: if (this.value.length > 11) this.value = this.value.slice(0, 11)'}
            elif arr == "profile_image":
                self.fields[arr].widget.attrs = {'class': 'dropify form-control w-56 block mx-auto',
                                                 'data-default-file': request.user.profile.get_profile_image_url.url,
                                                 'data-height': '180'}
            else:
                self.fields[arr].widget.attrs.update(
                    {'class': 'select2-search__field ', 'placeholder': 'Cinsiyet', 'required': 'true'})


class ContactUpload(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phoneNumber',)

    def __init__(self, request, *args, **kwargs):
        super(ContactUpload, self).__init__(*args, **kwargs)
        for arr in self.fields:
            self.fields[arr].widget.attrs.update({'class': 'select2-search__field ', 'required': 'required'})
