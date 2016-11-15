from django.shortcuts import render_to_response, redirect, render, HttpResponse
from django.template import RequestContext
from django.contrib.auth import login as django_login, authenticate, logout as django_logout
from .forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


def index_page(request):
    if(request.user.is_authenticated()):
        user = request.user
        print(user)
        context = { 'user':user }
        return render(request,'login.html',context)
    else:
        print("No")
        form = AuthenticationForm()
        context = {'form':form}
        return render(request,'index.html',context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['email']
            user = authenticate(username=form.cleaned_data['email'], password=form.cleaned_data['password'])
            if user is not None:
                django_login(request,user)
                context = { 'user':user}
                return render(request,'login.html',context)
            else:
                return HttpResponse("Please Check Your Credentials")
        else:
            return HttpResponse("Form is not valid")
    elif(request.user.is_authenticated()):
        user = request.user
        context = { 'user':user}
        return render(request,'login.html',context)
    else:
        form = AuthenticationForm()
        context = {'form':form}
        return render(request,'index.html',context)

@login_required
def logout(request):
    django_logout(request)
    return redirect('index')
