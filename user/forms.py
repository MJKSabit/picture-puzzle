import math

from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import *

ACC_TYPE = (
    (1, "Alumni"),
    (2, "Current Student"),
)


class UserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs = {'class': 'form-control', 'placeholder': 'User Handle',
                                                'required': 'required'}
        self.fields['email'].widget.attrs = {'class': 'form-control', 'placeholder': 'Email',
                                             'required': 'required'}
        self.fields['password1'].widget.attrs = {'class': 'form-control', 'placeholder': 'Password',
                                                 'required': 'required'}
        self.fields['password2'].widget.attrs = {'class': 'form-control', 'placeholder': 'Confirm Password',
                                                 'required': 'required'}

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class ParticipantForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ParticipantForm, self).__init__(*args, **kwargs)

        self.fields['acc_type'] = forms.ChoiceField(choices=ACC_TYPE)
        self.fields['acc_type'].widget.attrs = {'class': 'form-control', 'required': 'required'}

        self.fields['student_ID'] = forms.CharField(widget=forms.TextInput, max_length=7, min_length=7)
        self.fields['student_ID'].widget.attrs = {'class': 'form-control', 'required': 'required',
                                                  'placeholder': 'Student Id'}

    class Meta:
        model = Participant
        fields = ('acc_type', 'student_ID')

    def clean_student_ID(self, *args, **kwargs):
        std_id = self.cleaned_data.get('student_ID')

        if not std_id.isnumeric():
            raise forms.ValidationError("Student ID must be numeric.")

        acc_type = int(self.cleaned_data.get('acc_type'))

        batch = int(std_id[0:2])
        dept = int(std_id[2:4])
        roll = int(std_id[4:7])

        if dept != 5:
            raise forms.ValidationError("You're not from BUET CSE Department. Sorry.")

        if roll > 185:
            raise forms.ValidationError("This roll isn't valid.")

        if roll < 1:
            raise forms.ValidationError("This roll isn't valid.")

        if acc_type == 1 and batch not in range(1, 18):  # need to include 90's batches
            raise forms.ValidationError("this is not a valid id")

        if acc_type == 2 and batch not in [18, 19, 20, 21]:
            raise forms.ValidationError("You're not a current student, please select ALUMNI option from below.")

        return std_id
