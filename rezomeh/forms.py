from django import forms
from .models import Comment, Contact
from django.utils.translation import gettext_lazy as _

class CommentForm(forms.ModelForm):
    name = forms.CharField(label=_('name'))
    message = forms.CharField(label=_('message'))

    class Meta:
        model = Comment
        fields = ['name', 'message']

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label=_("Name"))
    email = forms.EmailField(required=True, label=_("Email"))
    message = forms.CharField(widget=forms.Textarea, required=True, label=_("Message"))