from django import forms

class ChoiceForm(forms.Form):
    def __init__(self, *args, **kwargs):
        choices = kwargs.pop("radio_choices", [])
        super(ChoiceForm, self).__init__(*args, **kwargs)
        
        self.fields["choice"] = forms.CharField(widget=forms.RadioSelect(choices=choices))