from django.db import models
from django.contrib.auth.models import AbstractUser 
# Create your models here.

class CustomUserForm(AbstractUser):
    enrollment = models.CharField(max_length=12)
    emailid = models.EmailField(max_length=254, default='xyz@gmail.com')
    karma_points = models.IntegerField(default=0, null=True, blank=True)
    
    def __str__(self):
        return self.username


class AboutModel(models.Model):
    username = models.CharField(max_length=150)
    about = models.TextField(max_length=500)

    def __str__(self):
        return self.username

class BookModel(models.Model):
    
    subject_name = models.CharField(max_length=100)
    course = models.CharField(max_length=50)
    author1 = models.CharField(max_length=30)
    author2 = models.CharField(max_length=30, null=True)
    publisher = models.CharField(max_length=70)
    tags1 = models.CharField(max_length=30)
    tags2 = models.CharField(max_length=30)
    tags3 = models.CharField(max_length=30)
    cover = models.ImageField(upload_to='images/', null=True, blank=True)
    uploaded_by = models.CharField(max_length=150, default='DEFAULT')
    pdffile = models.FileField(upload_to='documents/', default=None, null= True, blank=True)
    recieved = models.BooleanField(default=False)


    def __str__(self):
        return self.subject_name

class search(models.Model):
    searchq = models.CharField(max_length=150)

class SendMessageModel(models.Model):
    to = models.CharField(max_length=150)
    fromperson = models.CharField(max_length=150)
    frompost = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    edit_count = models.IntegerField(default=0)
    mainmessage = models.TextField(max_length=500)
    mail = models.EmailField(max_length=200, default="xyz@gmail.com")
    
class Question(models.Model):
    question = models.CharField(max_length=200)
    user = models.CharField(max_length=150, default="abcd")

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.TextField(max_length=500)
    upvotes = models.IntegerField(default=0)
    user = models.CharField(max_length=150, default="abcd")
    
class userbook(models.Model):
    bookid =  models.ForeignKey(BookModel,on_delete= models.CASCADE)
    user_name = models.ForeignKey(CustomUserForm,on_delete= models.CASCADE)


