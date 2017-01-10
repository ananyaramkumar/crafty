from crafty.models import Material
from django import forms

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        exclude = ["diy"]

    def __init__(self, *args, **kwargs):
        super(MaterialForm, self).__init__(*args, **kwargs)
        for key in self.fields:
            self.fields[key].help_text = None