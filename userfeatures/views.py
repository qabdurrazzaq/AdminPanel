from django.contrib.auth import logout, login, authenticate
from django.http import JsonResponse
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views.generic import FormView
from .forms import AddUserForm, UserLoginForm
from .models import User
import json
# Create your views here.

def user_view(request):
    try:
        users = User.objects.get(user=request.user)
    except:
        users = None
    context = {
        'users' : users,
    }
    return render(request,'user.html')

def login_view(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username,password=password)
        login(request,user)
        return HttpResponseRedirect(reverse('user'))
    
    context = {"form":form, "logging": True}
    return render(request, "form.html", context)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))

def view_all_users_view(request):
    try:
        users = User.objects.all()
    except:
        users = None
    context = {
        'users' : users,
    }
    return render(request,'userfeature/view_all_users.html',context)

def all_users_stats_view(request):
    try:
        users = User.objects.all()
    except:
        users = None
    if users is not None:
        superuser_count = User.objects.filter(is_superuser=True).count()
        add_user_count = User.objects.filter(add_user=True).count()
        del_user_count = User.objects.filter(del_user=True).count()
        view_user_count = User.objects.filter(view_user=True).count()
        edit_user_count = User.objects.filter(edit_user=True).count()
        user_stats_count = User.objects.filter(user_stats=True).count()
    context = {
        'users' : users,
        'add_user_count': add_user_count,
        'superuser_count':superuser_count,
    }
    return render(request,'userfeature/all_user_stats.html',context)

def add_new_user_view(request):
    if request.method == 'POST':
        form = AddUserForm(request.POST or None, request.FILES or None)
        form.save()
    else:
        form = AddUserForm()
    context={
        'form' : form,
    }
    return render(request,'userfeature/add_new_user.html',context)

def add_new_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        mobile_no = request.POST.get('mobile_no')
        dept_name = request.POST.get('dept_name')
        age = request.POST.get('age')
        address = request.POST.get('address')
        add_user = request.POST.get('add_user')
        del_user = request.POST.get('del_user')
        view_user = request.POST.get('view_user')
        edit_user = request.POST.get('edit_user')
        user_stats = request.POST.get('user_stats')
        response_data = {}
        new_user_form = AddUserForm(request.POST or None, request.FILES or None)
        if new_user_form.is_valid():
            new_user_form.save(commit=False)
            new_user_form.save()
            return HttpResponse(json.dumps(response_data),content_type="application/json")
        else:
            response = JsonResponse({"error": "there was an error"})
            response.status_code = 403
            return response
    else:
        return HttpResponse(json.dumps({"nothing to see": "this isn't happening"}),content_type="application/json")

def del_user_view(request):
    users = User.objects.all()
    context = {
        'users':users,
    }
    return render(request,'userfeature/del_user.html',context)

def del_user(request):
    user_id = request.POST.get('id')
    #print(user_id)
    try:
        del_user = User.objects.get(id = user_id)
        print(del_user.username)
    except:
        del_user = None
        #print(del_user)
    if del_user is not None:
        del_user.delete()
        pass
    response_data = {}
    return HttpResponse(json.dumps(response_data),content_type="application/json")

def edit_user_view(request):
    users = User.objects.all()
    context = {
        'users':users,
    }
    return render(request,'userfeature/edit_user.html',context)

def update_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        mobile_no = request.POST.get('mobile_no')
        dept_name = request.POST.get('dept_name')
        age = request.POST.get('age')
        address = request.POST.get('address')
        add_user = request.POST.get('add_user')
        del_user = request.POST.get('del_user')
        view_user = request.POST.get('view_user')
        edit_user = request.POST.get('edit_user')
        user_stats = request.POST.get('user_stats')
    user = User.objects.get(username=username)
    user.first_name = first_name
    user.mobile_no = mobile_no
    user.dept_name = dept_name
    user.age = age
    user.address = address
    if add_user == 'true':
        user.add_user = True
    if del_user == 'true':
        user.del_user = True
    if view_user == 'true':
        user.view_user = True
    if edit_user == 'true':
        user.edit_user = True
    if user_stats == 'true':
        user.user_stats = True
    user.set_password(password)
    user.save()
    response_data={}
    return HttpResponse(json.dumps(response_data),content_type="application/json")

def edit_single_user(request,username):
    user = User.objects.get(username=username)
    context = {
        'user':user,
    }
    return render(request,'userfeature/edit_user_form.html',context)