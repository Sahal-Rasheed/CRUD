from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import StudentModel

class UserRegisterMForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']
        
        widgets = {
            'first_name' : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your first name'}),
            'last_name' : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your last name'}),
            'username' : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your username'}),
            'email' : forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter your email'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        first = cleaned_data.get('first_name')
        last = cleaned_data.get('last_name')
        
        if first == last:
            msg = "first name and last name cannot be same"
            self.add_error('last_name',msg)



class LoginForm(forms.Form):

    Username = forms.CharField(max_length=100, widget=(forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your username'})))
    Password = forms.CharField(max_length=100, widget=(forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter your password'})))
    
class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = '__all__'

        widgets = {
            'first' : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your first name'}),
            'last' : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your last name'}),
            'age' : forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter your age'}),
            'email' : forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter your email'}),
            'phone' : forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter your phone'}),
            'address' : forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter your Address'}),

        }

        def clean(self):
            cleaned_data =  super().clean()
            first_name = cleaned_data.get('first')
            last_name = cleaned_data.get('last')
            age = cleaned_data.get('age')
            phone = cleaned_data.get('phone')
            

            if first_name == last_name:
                msg = 'Last name cannot be same as first name'
                self.add_error('last', msg)
            
            if age <= 0:
                msg = 'Age cannot be less than or equal to zero'
                self.add_error('age', msg)

            if len(str(phone))  != 10:
                msg = 'Phone Number Must Be 10 digits'
                self.add_error('phone', msg)