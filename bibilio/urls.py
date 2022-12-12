"""bibilio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import signin, signup,signout, home, book, createAuthor, author, editor, gender, createEditor, createGender, createBook, registration_views

urlpatterns = [
    path('home/', home),
    path('admin/', admin.site.urls),
    path('login/', signin, name='login'),
    path('signup/', registration_views, name ='signup'),
    path('signout/', signout, name = 'logout'),
    path('book/', book, name = 'book'),
    path('createAuthor/', createAuthor, name = 'createAuthor'),
    path('author/', author, name = 'author'),
    path('editor/', editor, name = 'editor'),
    path('gender/', gender, name = 'gender'),
    path('createEditor/', createEditor, name = 'createEditor'),
    path('createGender/', createGender, name = 'createGender'),
    path('createBook/', createBook, name = 'createBook'),
]
