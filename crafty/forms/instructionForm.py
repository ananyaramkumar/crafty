from crafty.models import Instruction
from django import forms

class InstructionForm(forms.ModelForm):
    class Meta:
        model = Instruction
        exclude = ["diy"]

    def __init__(self, *args, **kwargs):
        super(InstructionForm, self).__init__(*args, **kwargs)
        for key in self.fields:
            self.fields[key].help_text = None