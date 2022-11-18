from django.forms import ModelForm
from bibilio.models import Book, Author, Gender, Editor

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