from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from accounts.forms import CustomUserForm
from accounts.models import CustomUser


# Create your views here.

def register(req):

    if 'superu' in req.session:
        return redirect(owner_home)

    form = CustomUserForm()
    context = {"form": form}

    if req.method == 'POST':
        form = CustomUserForm(req.POST)

        if form.is_valid():

            if 'password1' != 'password2':
                messages.info(req, "Passwords don't match.")

            elif len('passwords1') < 8:
                messages.info(req, "Passwords lesser than limit.")

            else:
                form.save()
                messages.info(req, 'Account has been created.')
                return redirect('login')

    return render(req, 'accounts/register.html', context)


def login_view(req):

    if 'superu' in req.session:
        return redirect('owner')

    if req.method == 'POST':
        u_name = req.POST['username']
        pwd = req.POST['password']

        user = authenticate(username=u_name, password=pwd)

        if user.is_superuser:
            req.session['superu'] = u_name
            return redirect(owner_home)

        elif user is not None:
            return redirect(user_home)

    return render(req, 'registration/login.html')


def user_home(req):
    return render(req, 'accounts/home.html')


def owner_home(req):
    if 'superu' in req.session:
        user = CustomUser.objects.all()
        context = {'user': user}
        return render(req, 'accounts/owner.html', context)

    elif req.user is not None:
        return redirect('customer')

    return redirect(login_view)


def sign_out(req):
    if 'superu' in req.session:
        req.session.flush()
    return redirect('login')


def delete_view(req, id):
    user = CustomUser.objects.get(id=id)
    user.delete()
    return redirect('owner')


def update_view(req, id):
    user = CustomUser.objects.get(id=id)
    form = CustomUserForm(instance=user)
    context = {'form': form}

    if req.method == 'POST':
        form = CustomUserForm(req.POST, instance=user)
        if form.is_valid():
            form.save()
            print('saved')
            return redirect('owner')
    return render(req, 'accounts/edit.html', context)


def create_user(req):
    form = CustomUserForm()
    context = {'form': form}

    if req.method == 'POST':
        form = CustomUserForm(req.POST)

        if form.is_valid():
            form.save()
            print('User has been created')
            return redirect(owner_home)
        else:
            print(form.errors)
    return render(req, 'accounts/create.html', context)


def search_user(req):
    if req.method == 'POST':
        searched = req.POST['searched']
        user = CustomUser.objects.filter(first_name__contains=searched)
        return render(req, 'accounts/owner.html', {'searched': searched, 'user': user})

    else:
        return render(req, 'accounts/owner.html')
