# from django import forms
# # from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
# from crugapp.models import *
# from django.conf import settings
# User=settings.AUTH_USER_MODEL

# class SignUpForm(forms.ModelForm):
#     # username = forms.CharField(max_length=30)
#     # email = forms.EmailField(max_length=200)

#     class Meta:
#         model = User
#         fields = '__all__'
#         # fields = ('username', 'email', 'password1', 'password2', )


# from django import forms
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
# from django.forms import ModelForm, TextInput


# class UserRegisterForm(UserCreationForm):
#     email = forms.EmailField()
#     phone_no = forms.CharField(max_length=20)
#     first_name = forms.CharField(max_length=20)
#     last_name = forms.CharField(max_length=20)

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'phone_no', 'password1', 'password2']


# from django import forms
# from api.models import *
# class BankdetailsForm(forms.ModelForm):
#     class Meta:
#         model = Bankdetails
#         fields = '__all__'

#         # fields = ['account_holder_name', 'account_number', 'email'] #https://docs.djangoproject.com/en/3.0/ref/forms/widgets/
#         # widgets = { 'name': forms.TextInput(attrs={ 'class': 'form-control' }),
#         #     'email': forms.EmailInput(attrs={ 'class': 'form-control' }),
#         #     'contact': forms.TextInput(attrs={ 'class': 'form-control' }),
#       # }


# class userform(ModelForm):
#     class Meta:
#        model = User
#        fields = ('username','email', 'password','is_staff','is_active','is_superuser')
#     widgets={
#     'password':TextInput(attrs={'type':'password'})
#     }