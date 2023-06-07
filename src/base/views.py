from django.http import JsonResponse, Http404
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.contrib.auth.hashers import make_password, check_password
from .models import SavedPassword
from .forms import PasswordForm
from django.contrib.auth import get_user_model
from django.forms.models import model_to_dict

from .forms import (
		RegisterForm
	)

# Create your views here.
@login_required(login_url="login")
def main_home_view(request):
	form = PasswordForm()
	if request.method == "POST" and "addPass" in request.POST:
		form = PasswordForm(request.POST)
		if form.is_valid():
			form.save()
			form = PasswordForm()
	if request.method == "POST" and "editPass" in request.POST:
		ID = int(request.POST.get("passwordID"))
		getPass = SavedPassword.objects.get(id=ID)
		form = PasswordForm(request.POST, instance=getPass)
		if form.is_valid():
			form.save()
			form = PasswordForm()
	obj = SavedPassword.objects.all()
	context = {
		'passwords': obj,
		'form': form
	}
	return render(request, "home.html", context)

def home_view(request):
	if request.user.is_anonymous:
		messages.warning(request, "Please login to continue!")
	return main_home_view(request)

def login_view(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == "POST":
			username = request.POST.get("username")
			password = request.POST.get("password")

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.error(request, "Incorrect username or password!")
		context = {}
		return render(request, "login.html", context)

def register_view(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		Usr = get_user_model()
		usr = Usr.objects.all()
		if (len(usr) == 0):
			form = RegisterForm()
			if request.method == "POST":
				form = RegisterForm(request.POST)
				if form.is_valid():
					username = form.cleaned_data.get('username')
					email = form.cleaned_data.get('email')
					password1 = form.cleaned_data.get('password1')
					password2 = form.cleaned_data.get('password2')
					if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
						messages.error(request, "Account creation error! Check info and try again!")
					else:
						if check_password(password2, make_password(password1)) and check_password(password1, make_password(password2)):
							print(User.objects.create_superuser(username, email, password1))
							messages.success(request, "Account created successfully for " + username + "!")
							return redirect('login')
						else:
							messages.error(request, "Account creation error! Check info and try again!")
			context = {
				'form': form
			}
			return render(request, "register.html", context)
		else:
			messages.warning(request, "Already registered! Please login!")
			return redirect('login')

def logout_view(request):
	logout(request)
	return redirect('login')

@login_required(login_url="login")
def deletePass(request, id):
	try:
		if request.user.is_authenticated:
			SavedPassword.objects.get(id=id).delete()
			return redirect('home')
	except SavedPassword.DoesNotExist:
		raise Http404

@login_required(login_url="login")
def fetchPass(request, id):
	try:
		if request.user.is_authenticated:
			password = SavedPassword.objects.get(id=id)
			return JsonResponse(model_to_dict(password))
	except SavedPassword.DoesNotExist:
		raise Http404