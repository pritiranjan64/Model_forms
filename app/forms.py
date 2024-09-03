from django import forms
from app.models import *

class TopicForm(forms.ModelForm):
    class Meta():
        model=Topic
        fields='__all__'


class WebpageForm(forms.ModelForm):
    class Meta():
        model=Webpage
        fields='__all__'
        #fields=['topic_name','name']
        #exclude=['name']
        labels={'topic_name':'TopicName'}
        widgets={'url':forms.PasswordInput,'name':forms.Textarea}


class AccessRecordForm(forms.ModelForm):
    class Meta():
        model=AccessRecord
        fields='__all__'