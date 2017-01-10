from crafty.models import Diy
from django import forms

class DiyForm(forms.ModelForm):
    class Meta:
        model = Diy
        exclude = ['creator']

    def __init__(self, *args, **kwargs):
        super(DiyForm, self).__init__(*args, **kwargs)
        for key in self.fields:
            self.fields[key].help_text = None