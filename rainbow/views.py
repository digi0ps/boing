from django.contrib.auth import authenticate, login, logout
from rainbow.forms import loginForm, newForm, uploadForm
from django.shortcuts import render, get_object_or_404
from django.template.defaultfilters import slugify
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from botocore.client import Config
from rainbow.models import story
import boto3

try:
    from singularity import awsAuth
except ImportError:
    pass

# Create your views here.


def home(request):
    return render(request, 'home.html')


def fluff(request):
    stories = story.objects.all().order_by('-createdTime')
    return render(request, 'fluff.html', {'stories': stories, })


def post(request, postId, slug=""):
    storyInstance = story.objects.get(pk=postId)
    return render(request, 'post.html', {'story': storyInstance, })


def dashboard(request):
    form = loginForm()
    stories = story.objects.all().order_by('-createdTime')
    if request.method == 'POST' and request.POST:
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User._default_manager.get(username__iexact=username)
            user_auth = authenticate(username=user.username, password=password)
        except User.DoesNotExist:
            user_auth = None
        if user_auth is not None:
            login(request, user_auth)
            return HttpResponseRedirect(reverse('boing'))
        else:
            error = 1
            return render(request, 'login.html', {'form': form, 'error': error})
    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request, 'dashboard.html', {'stories': stories})
        else:
            return render(request, 'login.html', {'form': form, })


def logoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse('boing'))


def new(request):
    form = newForm()
    error = 0
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('fluff'))
    if request.method == 'POST' and request.POST:
        submittedForm = newForm(request.POST)
        if submittedForm.is_valid():
            instance = submittedForm.save(commit=False)
            instance.save()
            return HttpResponseRedirect("/fluff/" + str(instance.pk) + "-" + str(slugify(instance.title)))
        else:
            error = 1
            return render(request, 'new.html', {'form': submittedForm, 'error': error})
    else:
        return render(request, 'new.html', {'form': form})


def edit(request, postId):
    error = 0
    postRequested = get_object_or_404(story, pk=postId)
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('fluff'))
    if request.method == 'POST' and request.POST:
        updatedForm = newForm(request.POST)
        if updatedForm.is_valid():
            postRequested.title = request.POST['title']
            postRequested.createdTime = request.POST['createdTime']
            postRequested.story = request.POST['story']
            postRequested.save()
            return HttpResponseRedirect("/fluff/" + str(postRequested.pk) + "-" + str(slugify(postRequested.title)))
        else:
            error = 1
            return render(request, 'new.html', {'form': updatedForm, 'error': error})
    else:
        data = {'title': postRequested.title,
                'createdTime': postRequested.createdTime,
                'story': postRequested.story,
                }
        form = newForm(data)
        return render(request, 'new.html', {'form': form})


def concoct(request):
    form = uploadForm()
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('fluff'))
    if request.method == 'POST' and request.POST:
        uploadedForm = uploadForm(request.POST, request.FILES)
        if uploadedForm.is_valid():
            fileName = request.FILES['file'].name
            s3 = boto3.resource('s3',
                                aws_access_key_id=awsAuth.AWS_ACCESS_ID,
                                aws_secret_access_key=awsAuth.AWS_SECRET_KEY,
                                config=Config(signature_version='s3v4'))
            data = request.FILES['file']
            s3.Bucket('intellectualdude').put_object(Key='Photos/' + str(fileName),
                                                     Body=data,
                                                     ACL='public-read',
                                                     ServerSideEncryption='AES256')
            link = "https://s3.ap-south-1.amazonaws.com/intellectualdude/Photos/" + str(fileName).replace(" ", "+")
            return render(request, 'concoct.html', {'link': link})
    else:
        return render(request, 'concoct.html', {'form': form})
