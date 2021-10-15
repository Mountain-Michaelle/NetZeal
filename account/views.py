from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse 
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UsersRegistrationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def dashboard(request):
    return render(request,
                    'account/dashboard.html',
                    {'section': 'dashboard'})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
        
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('You are signed-in')
            
                else:
                    return HttpResponse('Wrong username or password entered')
            else:
                return HttpResponse('This account is disabled!')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form':form})


def register(request):
    if request.method == 'POST':
        user_form = UsersRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            #set the chosen password 
            new_user.set_password(
                        user_form.cleaned_data['password'])
            # save the user object 
            new_user.save() 
            return render(request, 
                        'account/register_done.html',
                        {'new_user': new_user})
    else:
        user_form = UsersRegistrationForm()
    return render(request,
                'account/register.html',
                {'user_form':user_form})