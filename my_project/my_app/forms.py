from django import forms
from django.core import validators
from my_app.models import UserInfo

def check_for(value):
    i = ['abc@ves.com','xyz@ves.com','sagar@ves.com']

    if value not in i:
            raise forms.ValidationError("You are not a Participant")

def check_for_rate(value):
    if value>5:
        raise forms.ValidationError("Rate between 1 to 5")

class UserForm(forms.ModelForm):

#    name = forms.CharField()
     email_address = forms.CharField(validators=[check_for])
     rating = forms.IntegerField(validators=[check_for_rate])
#    roll_no = forms.CharField()
#    feedback = forms.CharField(widget=forms.Textarea)
     class Meta():
          model = UserInfo
          fields = ('name','roll_no','feedback','rating','email_address')
