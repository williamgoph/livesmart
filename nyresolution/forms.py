from django import forms

class UserForm(forms.Form):
    firstname = forms.CharField(label='First Name', max_length=100)
    surname = forms.CharField(label='Surname', max_length=100)
    dob = forms.DateField(label='Date of Birth')
    email = forms.EmailField(label='Email')
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)  
  
class GoalForm(forms.Form):
    entry = forms.CharField(label = 'Blog Entry')
