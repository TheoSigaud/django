from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from bibilio.forms import BookForm, AuthorForm, GenderForm, EditorForm
from bibilio.models import Book, Author, Gender, Editor

def home(request):
    if request.user.is_authenticated:
        return render(request, 'bibilio/home.html')
    else:
        return redirect('/login')

def signup(request):
    if request.user.is_authenticated:
        return redirect('/home')
     
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
 
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username,password = password)
            login(request, user)
            return redirect('/home')
         
        else:
            return render(request,'bibilio/signup.html',{'form':form})
     
    else:
        form = UserCreationForm()
        return render(request,'bibilio/signup.html',{'form':form})

def signin(request):
    if request.user.is_authenticated:
        return redirect('/home')
     
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username =username, password = password)
 
        if user is not None:
            login(request,user)
            return redirect('/home')
        else:
            form = AuthenticationForm()
            return render(request,'bibilio/signin.html',{'form':form})
     
    else:
        form = AuthenticationForm()
        return render(request, 'bibilio/signin.html', {'form':form})

def signout(request):
    logout(request)
    return redirect('/signout/')


def createBook(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
 
        if form.is_valid():
            form.save()
            return redirect('/book')
     
    else:
        formBook = BookForm()
        formAuthor = AuthorForm()
        formGender = GenderForm()
        formEditor = EditorForm()
        return render(request, 'bibilio/createBook.html',{'formBook':formBook, 'formAuthor':formAuthor, 'formGender':formGender, 'formEditor':formEditor})

def createAuthor(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
 
        if form.is_valid():
            form.save()
            return redirect('/author')
    else:
        form = AuthorForm()
        return render(request, 'bibilio/createAuthor.html',{'form':form})     

def author(request):
    authors = Author.objects.all()

    return render(request, 'bibilio/author.html', {'authors':authors})          

def editor(request):
    editors = Editor.objects.all()

    return render(request, 'bibilio/editor.html', {'editors':editors})

def book(request):
    books = Book.objects.all()

    return render(request, 'bibilio/book.html', {'books':books})       

def gender(request):
    genders = Gender.objects.all()

    return render(request, 'bibilio/gender.html', {'genders':genders})         

def createEditor(request):
    if request.method == 'POST':
        form = EditorForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/editor')
    else:
        form = EditorForm()
        return render(request, 'bibilio/createEditor.html',{'form':form})

def createGender(request):
    if request.method == 'POST':
        form = GenderForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/gender')
    else:
        form = GenderForm()
        return render(request, 'bibilio/createGender.html',{'form':form})        