from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from bibilio.forms import BookForm, AuthorForm, GenderForm, EditorForm, GroupForm, ForumForm, LoanForm
from bibilio.models import Book, Author, Gender, Editor, Group, Forum, Loan
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
                return redirect('/library/book')
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
            return redirect('/library/book')
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
            return redirect('/library/author')
    else:
        form = AuthorForm()
        return render(request, 'bibilio/createAuthor.html',{'form':form})     

def author(request):
    authors = Author.objects.all()
    user = request.user
    #get user profile
    profile = Profile.objects.get(user=user)
    if profile.is_staff == 1:
        return render(request, 'bibilio/library/author.html', {'authors':authors})  
    else:
        return render(request, 'bibilio/author.html', {'authors':authors})  
            

def editor(request):
    editors = Editor.objects.all()
    user = request.user
    #get user profile
    profile = Profile.objects.get(user=user)
    if profile.is_staff == 1:
        return render(request, 'bibilio/library/editor.html', {'editors':editors})
    else:
        return render(request, 'bibilio/editor.html', {'editors':editors})


def book(request):
    if request.user.is_authenticated:
        books = Book.objects.all()
        user = request.user
        #get user profile
        profile = Profile.objects.get(user=user)
        if profile.is_staff == 1:
            return render(request, 'bibilio/library/book.html', {'books':books})  
        else:
            title = request.GET.get('title')
            editor_id = request.GET.get('editor')
            gender_id = request.GET.get('gender')
            if gender_id:
                books = books.filter(gender_id=gender_id)
            if title:
                books = books.filter(title__icontains=title)
            if editor_id:
                books = books.filter(editor_id=editor_id)
            editors = Editor.objects.all()
            genders = Gender.objects.all()
            return render(request, 'bibilio/book.html', {'books':books, 'editors':editors, 'genders':genders})  
    else:
        return redirect('/')

def group(request):
    group = Group.objects.all()

    return render(request, 'bibilio/group.html', {'group':group})

def forum(request):
    forum = Forum.objects.all()

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
    if request.user.is_authenticated:
        books = Book.objects.all()
        #get user object
        user = request.user
        #get user profile
        profile = Profile.objects.get(user=user)
        if profile.is_staff == 1:
            return render(request, 'bibilio/library/book.html', {'books':books})   
        else:
            return render(request, 'bibilio/book.html', {'books':books})   
    else:
        return redirect('/')
    

def gender(request):
    genders = Gender.objects.all()
    user = request.user
    #get user profile
    profile = Profile.objects.get(user=user)
    if profile.is_staff == 1:
        return render(request, 'bibilio/library/gender.html', {'genders':genders})         
    else:
        return render(request, 'bibilio/gender.html', {'genders':genders})         
            
    

def createEditor(request):
    if request.method == 'POST':
        form = EditorForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/library/editor')
    else:
        form = EditorForm()
        return render(request, 'bibilio/createEditor.html',{'form':form})

def createGender(request):
    if request.method == 'POST':
        form = GenderForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/library/gender')
    else:
        form = GenderForm()
        return render(request, 'bibilio/createGender.html',{'form':form}) 

def deleteGender(request):
    id=request.GET.get('id','Not available')
    get_object_or_404(Gender, pk=id).delete()
    return redirect('/library/gender')

def updateGender(request):
    id=request.GET.get('id','Not available')
    gender = Gender.objects.get(pk=id)
    if request.method == 'POST':
        form = GenderForm(request.POST, instance=gender)
 
        if form.is_valid():
            form.save()
            return redirect('/library/gender')
    else:
        form = GenderForm(instance=gender)

        return render(request, 'bibilio/updateGender.html',{'form':form})      

def deleteEditor(request):
    id=request.GET.get('id','Not available')
    get_object_or_404(Editor, pk=id).delete()
    return redirect('/library/editor')

def updateEditor(request):
    id=request.GET.get('id','Not available')
    editor = Editor.objects.get(pk=id)
    if request.method == 'POST':
        form = GenderForm(request.POST, instance=editor)
 
        if form.is_valid():
            form.save()
            return redirect('/library/editor')
    else:
        form = EditorForm(instance=editor)

        return render(request, 'bibilio/updateEditor.html',{'form':form})       

def deleteAuthor(request):
    id=request.GET.get('id','Not available')
    get_object_or_404(Author, pk=id).delete()
    return redirect('/library/author')

def updateAuthor(request):
    id=request.GET.get('id','Not available')
    author = Author.objects.get(pk=id)
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)

        if form.is_valid():
            form.save()
            return redirect('/library/author')
    else:
        form = AuthorForm(instance=author)

        return render(request, 'bibilio/updateAuthor.html',{'form':form}) 

def loanBook(request):
    #Get all Loan by profile
    if request.user.is_authenticated:
        user = request.user
        profile = Profile.objects.get(user=user)
        if profile.is_staff == 1:
            loan = Loan.objects.all()
            return render(request, 'bibilio/library/loanBook.html', {'loanBook':loan})  
        else:
            loan = Loan.objects.filter(profile=profile)
            return render(request, 'bibilio/loanBook.html', {'loanBook':loan})  
    else:
        return redirect('/')

def createLoanBook(request):
    id=request.GET.get('id','Not available')
    book = get_object_or_404(Book, pk=id)
    if request.method == 'POST':
        form = LoanForm(request.POST)
        if form.is_valid():  
            #adding profile to loan
            user = request.user
            profile = Profile.objects.get(user=user)
            form.instance.profile = profile
            form.instance.borrowed = 1
            form.save()
            form.instance.book.set([book])
            return redirect('/loanBook')
    else:
        form = LoanForm()
        return render(request, 'bibilio/loanBookCreate.html', {'form':form})

def deleteLoanBook(request, loan_id):
    loan = get_object_or_404(Loan, pk=loan_id)
    loan.borrowed = 0
    loan.save()
    return redirect('/loanBook')