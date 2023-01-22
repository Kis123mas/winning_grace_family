from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import CreateUserForm, MemberForm, PrayerForm, TestimonyForm, PostForm, CommentForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.models import Group
from django.utils.text import slugify



# Create your views here.
def landingPage(request):
    posts = Post.objects.all()[:4]
    events = Event.objects.all()[:3]
    context = {'posts': posts, 'events': events}
    return render(request, 'htmlfiles/landing_page.html',context)





@login_required(login_url='loginpage')
def profilePage(request):
    member = request.user.member
    form = MemberForm(instance=member)

    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES, instance=member)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request, 'htmlfiles/users-profile.html', context)





@login_required(login_url='loginpage')
def contactPage(request):
    return render(request, 'htmlfiles/pages-contact.html')


@login_required(login_url='loginpage')
def successPage(request):
    return render(request, 'htmlfiles/successful.html')


@login_required(login_url='loginpage')
def prayerPage(request):
    form = PrayerForm(request.POST)

    if request.method == 'POST':
        if form.is_valid:
            form.save()
            return redirect('/success')

    context = {
        "form":form
    }
    
    return render(request, 'htmlfiles/prayerform.html', context)
    



@login_required(login_url='loginpage')
def testimonyPage(request):
    form = TestimonyForm(request.POST)

    if request.method == 'POST':
        if form.is_valid:
            form.save()
            return redirect('/success')
            

    context = {
        "form":form
    }
    return render(request, 'htmlfiles/testimonyform.html', context)
    




@login_required(login_url='loginpage')
def calenderPage(request):
    return render(request, 'htmlfiles/calender.html')



@login_required(login_url='loginpage')
@allowed_users(allowed_roles=['member'])
def memberPage(request):
    posts = Post.objects.all()[:3]
    events = Event.objects.all()
    context = {'posts': posts, 'events': events}
    
    return render(request, 'htmlfiles/member.html', context)

 


@login_required(login_url='loginpage')
@admin_only
def homePage(request):
    return render(request, 'htmlfiles/home.html')




def registerationPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='member')
            user.groups.add(group)
            Member.objects.create(
                user=user,
            )

            messages.success(request, 'Congratulations! ' + username + ' Your account was created.')
            return redirect('loginpage')

    context = {'form':form}
    return render(request, 'htmlfiles/register.html', context)




@unauthenticated_user
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            messages.info(request, 'username OR password is incorrect')
    context = {}
    return render(request, 'htmlfiles/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('landingpage')


# blog views

@login_required(login_url='loginpage')
def bloghomePage(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'htmlfiles/bloghome.html', context)


@login_required(login_url='loginpage')
def detailblogPage(request, slug):
    post = Post.objects.get(slug=slug)
    posts = Post.objects.exclude(post_id__exact=post.post_id)[:4]
    context = {'post': post, 'posts':posts}
    return render(request, 'htmlfiles/blogdetail.html', context)


@login_required(login_url='loginpage')
def createPost(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid:
            post = form.save(commit=False)
            post.slug = slugify(post.title)
            post.save()
            messages.info(request, 'Article Created Successfully')
            return redirect('create')
    context = {'form':form}
    return render(request, 'htmlfiles/createpost.html', context)


@login_required(login_url='loginpage')
def updatePost(request, slug):
    post = Post.objects.get(slug=slug)
    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('detailpage', slug=post.slug)
    context = {'form':form}
    return render(request, 'htmlfiles/createpost.html', context)


@login_required(login_url='loginpage')
def deletePost(request, slug):
    post = Post.objects.get(slug=slug)
    form = PostForm(instance=post)
    if request.method == 'POST':
        post.delete()
        return redirect('bloghomepage')
    context = {'form':form}
    return render(request, 'htmlfiles/delete.html', context)


@login_required(login_url='loginpage')
def createComment(request, slug):
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.slug = slugify(Comment.post)
            post.save()
            return redirect('bloghomepage')
    context = {'form':form}
    return render(request, 'htmlfiles/comment.html', context)
