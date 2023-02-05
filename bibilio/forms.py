from django.forms import ModelForm
from bibilio.models import Book, Author, Gender, Editor, Group, Forum, Loan
from django import forms
from django.contrib.auth.forms import UserCreationForm
from bibilio.models import User

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'firstname']

class GenderForm(ModelForm):
    class Meta:
        model = Gender
        fields = ['name']

class EditorForm(ModelForm):
    class Meta:
        model = Editor
        fields = ['name']        

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'editor', 'gender', 'jacket']

class GroupForm(ModelForm):
    date_group = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    class Meta:
        model = Group
        fields = ['name', 'date_group']

class ForumForm(ModelForm):
    class Meta:
        model = Forum
        fields = ['title']

class RegisterForm(UserCreationForm):
  first_name = forms.CharField(label='First name', max_length=100)
  last_name = forms.CharField(label='Last name', max_length=100)
  email = forms.EmailField(label='Email', max_length=100)
  adress = forms.CharField(label='Adress', max_length=100)
  city = forms.CharField(label='City', max_length=100)
  zipCode = forms.CharField(label='Zip code', max_length=100)
  #is staff radio button
  is_staff = forms.BooleanField(label='Je suis libraire ', required=False)
  class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'adress', 'city', 'zipCode', 'password1', 'password2', 'is_staff')


class LoanForm(ModelForm):
    #profile get the current user
    
    date_end = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}), label="Date de retour")
    class Meta:
        model = Loan
        fields = ['date_end', 'book', 'borrowed']
