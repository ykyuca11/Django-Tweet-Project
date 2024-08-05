from django import forms
from django.forms import ModelForm
from tweetapp.models import Tweet #, Image

class AddTweetForm(forms.Form):
    messageInput = forms.CharField(label="Mesaj",max_length=200)


class AddTweetModelForm(ModelForm):
    class Meta:
        model = Tweet
        fields = ["username","message","image"]


