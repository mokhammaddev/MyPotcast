from django import forms
from .models import Comment, Newsletter


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            "class": "comment_input comment_textarea",
            "placeholder": "name",
            "required": "required",

        })
        self.fields['message'].widget.attrs.update({
            "type": "text",
            "class": "comment_input",
            "placeholder": "Message",
            "required": "required"
        })


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({
            'type': 'email',
            'class': 'newsletter_input',
            'required': 'required',

        })


