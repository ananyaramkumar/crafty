from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
   
        for key in self.fields:
            self.fields[key].widget.attrs.update({'placeholder' : " ".join(key.split("_"))})
            self.fields[key].help_text = None
            self.fields[key].required = True