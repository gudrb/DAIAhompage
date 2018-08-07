from django import forms
from .models import Newmember
class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )
'''
class NameForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(), initial='0')
    email = forms.CharField(widget=forms.TextInput(), initial='0')
    password = forms.CharField(widget=forms.TextInput(), initial='0')
    git = forms.CharField(widget=forms.TextInput(), initial='0')
    sns = forms.CharField(widget=forms.TextInput(), initial='0')
    student_id = forms.IntegerField(widget=forms.TextInput(), initial='0')
    phone_num = forms.IntegerField(widget=forms.TextInput(), initial='0')
    #image = forms.FileField(upload_to=None, max_length=100)
'''

class ModelNameForm(forms.ModelForm):
    class Meta:
        model = Newmember #나중에 view에서 form.save() 할 경우 Newmember데이터 베이스에 정보가 저장됨
        fields= '__all__'