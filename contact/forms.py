from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            "type": "text",
            "class": "contact_input",
            "placeholder": "name",
            "required": "required",
        })
        self.fields['message'].widget.attrs.update({
            "type": "text",
            "class": "contact_input",
            "placeholder": "message",
            "required": "required",
        })

