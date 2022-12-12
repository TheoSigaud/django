from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from bibilio.forms import BookForm, AuthorForm, GenderForm, EditorForm
from bibilio.models import Book, Author, Gender, Editor
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm, authenticate
from .forms import RegisterForm
from .models import Profile, User

def registration_views(request):
    context = {}
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')            
            # modify the Profile table
            # get the user id
            user_id = request.user.id
            # get the user object
            user = User.objects.get(id=user_id)
            # get the user profile
            profile = Profile.objects.get(user=user)
            # modify the profile
            profile.address = form.cleaned_data.get('adress')
            profile.city = form.cleaned_data.get('city')
            profile.zipcode = form.cleaned_data.get('zipCode')
            # save the profile
            profile.save()
            return redirect('/home/')
        else:
            context['registration_form'] = form
    else:
        form = RegisterForm()
        context['registration_form'] = form
    return render(request, 'bibilio/signup.html', context)

def home(request):
    if request.user.is_authenticated:
        return render(request, 'bibilio/home.html')
    else:
        return redirect('/login')

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
    return redirect('/home/')

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