"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpRequest
from .forms import FeedbackPoolingForm, UserCreationForm, CommentCreationForm, ThreadCreationForm, PostCreationForm
from .models import SinglePost, Thread, ThreadComment

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    posts = SinglePost.objects.all()
    threads = Thread.objects.all()
    return render(
        request,
        'app/index.html',
        {
            'title': 'Коллектив осведомленных',
            'posts': posts,
            'threads': threads,
            'year': datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Связаться',
            'message':'Вы не можете связаться с нами.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'О WTEDS',
            'message':'Открываем глаза с ████ г.',
            'year':datetime.now().year,
        }
    )

def links(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/links.html',
        {
            'title': 'Ссылки',
            'message': 'Узнайте больше',
            'year': datetime.now().year,
        }
    )

def video(request):
    """Renders the video page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/video.html',
        {
            'year':datetime.now().year,
        }
    )

def pool(request):
    assert isinstance(request, HttpRequest)
    if request.method == "POST":
        form=FeedbackPoolingForm(request.POST)
        if form.is_valid():
            return render(
                request,
                'app/pool.html',
                {
                    'title': "Благодарим за отзыв",
                    'message': "",
                    'form': form,
                    'completed': True,
                    'year': datetime.now().year,
                }
            )
        else:
            message=form.errors
            return render(
                request,
                'app/pool.html',
                {
                    'title': "Отзыв заполнен неверно",
                    'message': message,
                    'form': form,
                    'completed': False,
                    'year': datetime.now().year,
                }
            )
    else:
        return render(
            request,
            'app/pool.html',
            {
                'title': 'Связь с просвещенными',
                'message': 'Дайте нам знать о том, о чем нужно знать',
                'form': FeedbackPoolingForm(),
                'completed': False,
                'year': datetime.now().year,
            }
        )

def registration(request):

    """Renders the registration page."""

    assert isinstance(request, HttpRequest)
    if request.method == "POST":

        regform = UserCreationForm(request.POST)

        if regform.is_valid():
            reg_f = regform.save(commit=False)
            reg_f.is_staff = False
            reg_f.is_active = True
            reg_f.is_superuser = False
            reg_f.date_joined = datetime.now()
            reg_f.last_login = datetime.now()
            reg_f.save()
            return redirect('home')

    else:

        regform = UserCreationForm()

        return render(
            request,
            'app/registrator.html',
            {
                'regform': regform,
                'year':datetime.now().year,
            }
        )

def create(request, type):
    assert isinstance(request, HttpRequest)
    if type not in ["post", "thread"]:
        return redirect('home')
    if request.method == "POST":
        if type == "post":
            form = PostCreationForm(request.POST, request.FILES)
            if form.is_valid():
                usr = None
                if (str(request.user) != "AnonymousUser"):
                    usr = request.user
                post = SinglePost(
                    title = form.cleaned_data["title"],
                    author = usr,
                    short_desc = form.cleaned_data["short_desc"],
                    text = form.cleaned_data["text"],
                    image_1 = form.cleaned_data["image_1"],
                    image_2 = form.cleaned_data["image_2"],
                    image_3 = form.cleaned_data["image_3"],
                )
                post.save()
                return redirect("singlepost", postid = post.id)
        else: 
            form = ThreadCreationForm(request.POST, request.FILES)
            if form.is_valid():
                usr = None
                if (str(request.user) != "AnonymousUser"):
                    usr = request.user
                thread = Thread(
                    title = form.cleaned_data["title"],
                    owner = usr,
                    short_desc = form.cleaned_data["short_desc"],
                    theme = form.cleaned_data["theme"],
                    image = form.cleaned_data["image"]
                )
                thread.save()
                return redirect("thread", threadid = thread.id)
    else:
        if type == "post":
            form = PostCreationForm()
        else: 
            form = ThreadCreationForm()
        return render(
            request,
            'app/create.html',
            {
                'type': type,
                'form': form,
                'year': datetime.now().year
            })



def singlepost(request, postid):
    assert isinstance(request, HttpRequest)
    post = SinglePost.objects.get(id = postid)
    return render(
        request,
        'app/postpage.html',
        {
            'post': post,
            'year': datetime.now().year
        }
    )

def thread(request, threadid):
    assert isinstance(request, HttpRequest)
    thread = Thread.objects.get(id = threadid)
    comments = ThreadComment.objects.filter(homethread__exact = threadid)
    if (request.method == "POST"):
        fform = CommentCreationForm(request.POST, request.FILES)
        if (fform.is_valid()):
            usr = None
            if fform.cleaned_data["provideas"] != "anon":
                if str(request.user) == "AnonymousUser":
                    return render(
                        request,
                        'app/thread.html',
                        {
                            'thread': thread,
                            'comments': comments,
                            'message': "Вы должны войти в аккаунт, чтобы оставлять сообщения как пользователь.",
                            'commform': fform,
                            'year': datetime.now()
                        }
                   )
                else:
                    usr = request.user
            comment = ThreadComment(
                author = usr,
                text = fform.cleaned_data["text"],
                homethread = thread,
                image_1 = fform.cleaned_data["image_1"],
                image_2 = fform.cleaned_data["image_2"],
                image_3 = fform.cleaned_data["image_3"],)
            comment.save()
            thread.active = datetime.now()
            thread.save()
            return render(
                request,
                'app/thread.html',
                {
                    'thread': thread,
                    'comments': comments,
                    'commform': CommentCreationForm(),
                    'year': datetime.now()
                }
            )
    else:
        return render(
            request,
            'app/thread.html',
            {
                'thread': thread,
                'comments': comments,
                'commform': CommentCreationForm(),
                'year': datetime.now()
            }
        )