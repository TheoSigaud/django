from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Editor(models.Model):
    name = models.CharField(max_length=255)   

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=255)     
    firstname = models.CharField(max_length=255)    

    def __str__(self):
        return self.name + ' ' + self.firstname 

class Gender(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    firstname = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    role = models.CharField(max_length=255, null=True)
    zipcode = models.IntegerField(null=True)
    is_staff = models.BooleanField(null=True)

class Library(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zipcode = models.IntegerField()
    profile = models.ManyToManyField(Profile)
    
class Book(models.Model):
    title = models.CharField(max_length=255)
    jacket = models.CharField(max_length=255)
    editor = models.ForeignKey(Editor, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)

class Session(models.Model):
    date = models.DateTimeField()

class Group(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    profile = models.ManyToManyField(Profile)
    
class Loan(models.Model):
    book = models.ManyToManyField(Book)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    date_loan = models.DateTimeField(null=True, blank=True)
    date_end = models.DateTimeField(null=True, blank=True)
    borrowed = models.BooleanField()



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()    