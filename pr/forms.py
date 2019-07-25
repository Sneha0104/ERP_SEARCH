from django import forms
from .models import PRHead

class PRChoiceForm(forms.ModelForm):
    class Meta:
        model = PRHead
        fields = ('pr_no',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['pr_no'].queryset = PRHead.objects.all()