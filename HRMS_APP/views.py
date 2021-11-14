# Copyright 2021 Allah
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages

def index_view(request):
	return render(request,'index_main.html')

def user_login(request):
    if not request.method == "POST":
        return render(request,"login/user_login.html")
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        auth_login(request,user)
        return redirect("/") # return redirect("/employee/")
    return render(request,"login/user_login.html")
    

def user_register(request):
    if not request.method == "POST":
        return render(request,"register/user_register.html")
    if request.user.is_authenticated:
        return redirect("/") # return redirect("/employee/")
    username = request.POST["username"]
    email = request.POST["email"]
    password = request.POST["password"]
    try:
        userexist = User.objects.get(username=username)
    except User.DoesNotExist:
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        auth_login(request,user)
        return redirect("/") # return redirect("/employee/")
    return render(request, "register/user_register.html")

def user_logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect("/")
    # return HttpResponseRedirect(reverse("home"))