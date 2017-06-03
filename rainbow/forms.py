from django.contrib.auth.models import User
from django.forms import ModelForm
from rainbow.models import story
from django import forms


class loginForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']


class newForm(ModelForm):
    createdTime = forms.DateField(widget=forms.DateInput(),
                                  label="Date (mm/dd/yyyy)")
    story = forms.CharField(widget=forms.Textarea(attrs={':value': 'input',
                                                         '@input': 'update',
                                                         }
                                                  ), label="The magic")

    class Meta:
        model = story
        fields = ['title', 'createdTime', 'story', ]


class uploadForm(forms.Form):
    file = forms.FileField(label="", widget=forms.FileInput(attrs={'class': 'upload'}))
