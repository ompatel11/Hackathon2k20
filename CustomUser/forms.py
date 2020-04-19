from django import forms
from .models import CustomUserForm, AboutModel, BookModel, search, SendMessageModel, Question, Answer
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUserForm
        fields = ('enrollment', 'username', 'emailid')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUserForm
        fields = ('enrollment', 'username', 'emailid')

class AboutForm(ModelForm):
    class Meta:
        model = AboutModel
        fields = ('username', 'about')

class BookForm(ModelForm):
    class Meta:
        model = BookModel
        fields = ['subject_name', 'course', 'author1', 'author2', 'publisher', 'tags1', 'tags2', 'tags3', 'cover', 'uploaded_by', 'pdffile']

class SearchForm(ModelForm):
    class Meta:
        model = search
        fields = ('searchq',)

class SendMessageForm(ModelForm):
    class Meta:
        model = SendMessageModel
        fields = (
            'mainmessage',
        )

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ('question',)

class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ('answer', 'upvotes')