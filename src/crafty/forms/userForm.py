from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['confirm_password'] = forms.CharField()
        self.fields['confirm_password'].widget = forms.PasswordInput()

        for key in self.fields:
            self.fields[key].help_text = None
            self.fields[key].required = True