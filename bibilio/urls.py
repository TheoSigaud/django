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
from django.conf import settings
from django.conf.urls.static import static
from .views import signin,signout, home, book, createAuthor, author, editor, gender, createEditor, createGender, createBook, registration_views, deleteBook, updateBook, deleteGender, updateGender, deleteEditor, updateEditor, deleteAuthor, updateAuthor, home, createGroup, group, deleteGroup, updateGroup, listGroup, forum, createForum, messageForum, createMessage, listGroup, joinGroup, leaveGroup

urlpatterns = [
    path('home/', home),
    path('admin/', admin.site.urls),
    path('', signin, name='login'),
    path('signup/', registration_views, name ='signup'),
    path('signout/', signout, name = 'logout'),
    path('book/', book, name = 'book'),
    path('home/', home, name = 'home'),
    path('createAuthor/', createAuthor, name = 'createAuthor'),
    path('author/', author, name = 'author'),
    path('editor/', editor, name = 'editor'),
    path('gender/', gender, name = 'gender'),
    path('createEditor/', createEditor, name = 'createEditor'),
    path('createGender/', createGender, name = 'createGender'),
    path('createBook/', createBook, name = 'createBook'),
    path('book/delete/', deleteBook, name = 'deleteBook'),
    path('book/update/', updateBook, name = 'updateBook'),
    path('gender/delete/', deleteGender, name = 'deleteGender'),
    path('gender/update/', updateGender, name = 'updateGender'),
    path('editor/delete/', deleteEditor, name = 'deleteEditor'),
    path('editor/update/', updateEditor, name = 'updateEditor'),
    path('author/delete/', deleteAuthor, name = 'deleteAuthor'),
    path('author/update/', updateAuthor, name = 'updateAuthor'),
    path('createGroup/', createGroup, name = 'createGroup'),
    path('createForum/', createForum, name = 'createForum'),
    path('group/', group, name = 'group'),
    path('group/delete/', deleteGroup, name = 'deleteGroup'),
    path('group/update/', updateGroup, name = 'updateGroup'),
    path('forum/messageForum/', messageForum, name = 'messageForum'),
    path('forum/', forum, name='forum'),
    path('listGroup/', listGroup, name='listGroup'),
    path('joinGroup/', joinGroup, name='joinGroup'),
    path('leaveGroup/', leaveGroup, name='leaveGroup'),
    path('createMessage/', createMessage, name='createMessage'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
