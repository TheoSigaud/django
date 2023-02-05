from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from bibilio.forms import BookForm, AuthorForm, GenderForm, EditorForm, GroupForm, ForumForm
from bibilio.models import Book, Author, Gender, Editor, Group, Forum
from django.contrib.auth.forms import AuthenticationForm, authenticate
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
            profile.firstname = form.cleaned_data.get('first_name')
            profile.name = form.cleaned_data.get('last_name')
            profile.is_staff = form.cleaned_data.get('is_staff')
            # save the profile
            profile.save()
            return redirect('/home/')
        else:
            context['registration_form'] = form
    else:
        form = RegisterForm()
        context['registration_form'] = form
    return render(request, 'bibilio/signup.html', context)


# def home(request):
#     if request.user.is_authenticated:
#         return render(request, 'bibilio/home.html')
#     else:
#         return redirect('/login')

def signin(request):
    if request.user.is_authenticated:
        return redirect('/home')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username =username, password = password)
        
        if user is not None:
            login(request,user)
            #get user object
            user = User.objects.get(username=username)
            #get user profile
            profile = Profile.objects.get(user=user)
            if profile.is_staff == 1:
                return redirect('/library')
            else:
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
        form = BookForm(request.POST, request.FILES)

        if form.is_valid():
            
            form.save()
        return redirect('/book')
    else:
        formBook = BookForm()
        formAuthor = AuthorForm()
        formGender = GenderForm()
        formEditor = EditorForm()
        return render(request, 'bibilio/createBook.html',{'formBook':formBook, 'formAuthor':formAuthor, 'formGender':formGender, 'formEditor':formEditor})  

def createGroup(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)

        if form.is_valid():
            
            form.save()
        return redirect('/group')
    else:
        form = GroupForm()
        return render(request, 'bibilio/createGroup.html',{'form':form})

def deleteBook(request):
    id=request.GET.get('id','Not available')
    get_object_or_404(Book, pk=id).delete()
    return redirect('/book')

def updateBook(request):
    id=request.GET.get('id','Not available')
    book = Book.objects.get(pk=id)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
 
        if form.is_valid():
            form.save()
            return redirect('/book')
    else:
        formAuthor = AuthorForm()
        formGender = GenderForm()
        formEditor = EditorForm()
        formBook = BookForm(instance=book)

        return render(request, 'bibilio/updateBook.html',{'formBook':formBook, 'formAuthor':formAuthor, 'formGender':formGender, 'formEditor':formEditor})      

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

def group(request):
    group = Group.objects.all()

    return render(request, 'bibilio/group.html', {'group':group})

def forum(request):
    forum = Forum.objects.all()
    print(request.user.id)

    return render(request, 'bibilio/forum.html', {'forum':forum})

def listGroup(request):
    group = Group.objects.all()

    return render(request, 'bibilio/listGroup.html', {'group':group})

def deleteGroup(request):
    id = request.GET.get('id', 'Not available')
    get_object_or_404(Group, pk=id).delete()
    return redirect('/group')


def updateGroup(request):
    id = request.GET.get('id', 'Not available')
    group = Group.objects.get(pk=id)
    if request.method == 'POST':
        form = GroupForm(request.POST, request.FILES, instance=group)

        if form.is_valid():
            form.save()
            return redirect('/group')
    else:
        formGroup = GroupForm(instance=group)

        return render(request, 'bibilio/updateGroup.html',
                      {'form': formGroup})

def home(request):
    books = Book.objects.all()

    return render(request, 'bibilio/home.html', {'books':books})           

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

def createForum(request):
    if request.method == 'POST':
        form = ForumForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/forum')
    else:
        form = ForumForm()
        return render(request, 'bibilio/createForum.html',{'form':form})

def createGender(request):
    if request.method == 'POST':
        form = GenderForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/gender')
    else:
        form = GenderForm()
        return render(request, 'bibilio/createGender.html',{'form':form}) 

def deleteGender(request):
    id=request.GET.get('id','Not available')
    get_object_or_404(Gender, pk=id).delete()
    return redirect('/gender')

def updateGender(request):
    id=request.GET.get('id','Not available')
    gender = Gender.objects.get(pk=id)
    if request.method == 'POST':
        form = GenderForm(request.POST, instance=gender)
 
        if form.is_valid():
            form.save()
            return redirect('/gender')
    else:
        form = GenderForm(instance=gender)

        return render(request, 'bibilio/updateGender.html',{'form':form})      

def deleteEditor(request):
    id=request.GET.get('id','Not available')
    get_object_or_404(Editor, pk=id).delete()
    return redirect('/editor')

def updateEditor(request):
    id=request.GET.get('id','Not available')
    editor = Editor.objects.get(pk=id)
    if request.method == 'POST':
        form = GenderForm(request.POST, instance=editor)
 
        if form.is_valid():
            form.save()
            return redirect('/editor')
    else:
        form = EditorForm(instance=editor)

        return render(request, 'bibilio/updateEditor.html',{'form':form})       

def deleteAuthor(request):
    id=request.GET.get('id','Not available')
    get_object_or_404(Author, pk=id).delete()
    return redirect('/author')

def updateAuthor(request):
    id=request.GET.get('id','Not available')
    author = Author.objects.get(pk=id)
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
 
        if form.is_valid():
            form.save()
            return redirect('/author')
    else:
        form = AuthorForm(instance=author)

        return render(request, 'bibilio/updateAuthor.html',{'form':form}) 