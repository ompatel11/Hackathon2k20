from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserChangeForm, AboutForm, BookForm, SearchForm, SendMessageForm, QuestionForm, AnswerForm
from .models import AboutModel, BookModel, SendMessageModel, Question, Answer , userbook, CustomUserForm, AbstractUser
import json
from django.http import HttpResponse
from django.db.models import Q
from django.templatetags.static import static
import re

# Create your views here.
def GetResult(string):
    return BookModel.objects.filter(
        Q(tags1__icontains=string) | Q(tags2__icontains=string) | Q(tags3__icontains=string)
    )


def empty(request):
    return redirect('home')
    return render(request, 'CustomUser/empty.html')

def home(request):
    if request.method == "POST":
        fo = SearchForm(request.POST)
        if fo.is_valid():
            fo.save()
            print("valid")
            temp = GetResult(request.POST['searchq'])
            searchform = SearchForm
            if temp:
                return render(request, 'CustomUser/BookSelf/new_home/index.html', {"temp" : temp, "search" : searchform})
            else:
                return render(request, 'CustomUser/BookSelf/new_home/index.html', {"temp" : "not found", "search" : searchform})
        else:
            print("invalid")

    searchform = SearchForm
    alldata = BookModel.objects.all().order_by('-id')
    return render(request, 'CustomUser/BookSelf/new_home/index.html', {"search" : searchform, "alldata" : alldata[:5]})

def signup2(request):
    if request.method == "POST":
        enrollment = request.POST['enrollment']
        username = request.POST['username']
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('login')
        else:
            return render(request, 'CustomUser/BookSelf/signup/index.html', {'form': form})

    else:
        form = CustomUserCreationForm
        return render(request, 'CustomUser/BookSelf/signup/index.html', {'form': form})
        
def about(request, usernameurl):
    f = AboutModel.objects.filter(username=usernameurl)
    if f:      
        return render(request, 'CustomUser/about.html', {"form" : f, "currentuser": request.user, "username" : f[0].username})
    else:
        return redirect('editabout')
        
def contact(request):
    def getneccessary():
        return SendMessageModel.objects.filter(
        Q(to__icontains=request.user) | Q(fromperson__icontains=request.user)
    )
    getall = getneccessary()
    return render(request, 'CustomUser/BookSelf/notification_msg/split_screen/index.html', {"data" : getall})

def AboutEdit(request):
    if request.method == "POST":
        PostForm = AboutForm(request.POST)
        if PostForm.is_valid():
            temp = AboutModel.objects.filter(username=request.user)
            if temp:
                temp = AboutModel.objects.get(username=request.user)
                temp.about = request.POST['about']
                temp.save()
            else:
                PostForm.save()
            return redirect('about', usernameurl=request.user)
        else:
            return render(request, 'CustomUSer/temp.html', {"form" : PostForm})
    else:
        form = AboutForm
        temp = AboutModel.objects.filter(username=request.user)
        if temp:
            temp = AboutModel.objects.get(username=request.user)
            ab = temp.about
        else:
            return render(request, 'CustomUser/AboutEdit.html', {"username" : request.user, "form" : form})
        
    return render(request, 'CustomUser/AboutEdit.html', {"username" : request.user, "form" : form, "ab" : ab})

def donate(request):
    if request.method == "POST":
        submitted = BookForm(request.POST, request.FILES)
        if submitted.is_valid():
            
            temp = submitted.save()
            a = CustomUserForm.objects.get(username=request.user)
            a.karma_points += 7
            a.save()
            print("hello world")
            return redirect('AskForUploadRecieve')
        else:
            form = BookForm
            print("not valid donaes")
            return render(request, "CustomUser/BookSelf/upload/index.html", {"form": submitted})

    form = BookForm
    
    return render(request, 'CustomUser/BookSelf/upload/index.html', {"form" : form})

def displaydonate(request, donatepage):
    if request.POST[(request.POST['textfield'])]:
        print("hello world")
        return HttpResponse('hellowrld')

    requested_object = BookModel.objects.get(pk=donatepage)
    similar = GetResult(requested_object.tags1)
    similar = similar | (GetResult(requested_object.tags2))
    similar = similar | GetResult(requested_object.tags3)
    return render(request, 'CustomUser/BookSelf/display/index.html', {"displayinfo" : requested_object, "similar" : similar})

def sendmessage(request, postid, to, fromperson):
    if request.method == "POST":
        messageform = SendMessageForm(request.POST)
        if messageform.is_valid():
            messageobject = SendMessageModel(to=to, fromperson=fromperson, frompost=postid, mainmessage=messageform.cleaned_data['mainmessage'])
            messageobject.save()
            return redirect('sentmsg')
    form = SendMessageForm
    return render(request, 'CustomUser/SendMessage.html', {"form" : form})

def ask(request):
    if request.method == "POST":
        submitted = QuestionForm(request.POST)
        ques = request.POST["question"]
        q = Question(question=ques, user=request.user)
        q.save()
        return redirect('home')
    form = QuestionForm
    return render(request, 'CustomUser/discuss.html',{"form" : form})

def topics(request):
    questions = Question.objects.all()
    return render(request, 'CustomUser/topics.html', {"questions": questions})

def topic_specific(request, id):
    if request.method == "POST":
        object = Question.objects.get(pk=id)
        submitted = AnswerForm(request.POST)
        desc = request.POST["answer"]
        saved = Answer(question=object,answer=desc,upvotes=0, user=request.user)
        saved.save()
        temp = object.answer_set.all()
        return redirect("topic_specific", id=id)
    object = Question.objects.get(pk=id)
    temp = object.answer_set.all()
    form = AnswerForm
    return render(request, 'CustomUser/topic_specific.html', {"object":object, "form":form, "temp":temp})

def UpRec(request):
    return render(request, 'CustomUser/BookSelf/split_screen/index.html')

def searchbox(request):
    if request.method == "POST":
        fo = SearchForm(request.POST)
        if True:
            fo.save()
            print("valid")
            temp = GetResult(request.POST['searchq'])
            print(temp)
            searchform = SearchForm
            if temp:
                return render(request, 'CustomUser/BookSelf/display/index.html', {"temp" : temp, "search" : searchform})
            else:
                return render(request, 'CustomUser/BookSelf/display/index.html', {"temp" : "not found", "search" : searchform})
        else:
            print("invalid")

    searchform = SearchForm
    alldata = BookModel.objects.all().order_by('-id')
    return render(request, 'CustomUser/BookSelf/search/index.html', {"search" : searchform, "alldata" : alldata[:5]})

def reward(request):

    return render(request, 'CustomUser/BookSelf/rewards/index.html',{"points":request.user, "trees":int(request.user.karma_points/7)})

def pdf_split(request):
    return render(request, 'CustomUser/BookSelf/split_screen/upload_pdf_physical.html')

def pdf_upload(request):
    if request.method == "POST":
        bname  = request.POST['subject_name']
        t = bname[0]
        a = BookModel(subject_name=request.POST['subject_name'], course=request.POST['course'], author1=request.POST['author1'], author2=request.POST['author2'], publisher=request.POST['publisher'], tags1=request.POST['tags1'], tags2=request.POST['tags2'], tags3=request.POST['tags3'],pdffile=request.FILES['cover'], cover=static("/BookSelf/logo/" + t + ".png"), uploaded_by="ompatel")
        a.save()
        return redirect('AskForUploadRecieve')

    return render(request, 'CustomUser/BookSelf/upload/index2.html')

def sentmsg(request):
    if request.method == "POST":
        a = BookModel.objects.get(pk=request.POST['text'])
        
        a.delete()
        
        return redirect('sentmsg')

    def getneccessary():
        return SendMessageModel.objects.filter(
        Q(fromperson__icontains=request.user)
    )
    getall = getneccessary()
    return render(request, 'CustomUser/BookSelf/notification_msg/sent_request/index.html', {"data" : getall})

def recvmsg(request):
    def getneccessary():
        return SendMessageModel.objects.filter(
        Q(to__icontains=request.user)
    )
    getall = getneccessary()
    return render(request, 'CustomUser/BookSelf/notification_msg/recieved_request/index.html', {"data" : getall})

def sendmsg(request):
    return render(request, 'CustomUser./BookSelf/notification_msg/split_screen/index.html')
