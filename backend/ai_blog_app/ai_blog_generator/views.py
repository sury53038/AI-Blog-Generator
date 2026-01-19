from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from pytube import youtube


# Create your views here.
@login_required
def index(request):
    return render(request, 'index.html')

def user_login(request):
    error_message = None

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            error_message = "Invalid username or password."

    return render(request, 'login.html', {'error_message': error_message})

def user_signup(request):
    if request.method == 'POST':
        username=request.POST['username']
        email=request.POST['email'] 
        password= request.POST['password']
        repeatpassword= request.POST['repeatPassword']

        if password == repeatpassword:
            try:
                user = User.objects.create_user(username, email, password)
                user.save()
                login(request, user)
                return redirect('/')
            except:
                error_message = 'Error creating account'
                return render(request, 'signup.html', {'error_message': error_message})
        else:
            error_message = "Password do not match."
            return render(request, 'signup.html', {'error_message': error_message})
    return render (request, 'signup.html')

def user_logout(request):
    logout(request)
    return redirect('/login')


@csrf_exempt
def generate_blog(request):
    if request.method == 'POST':
        try:
            data = json.load(request.body)
            yt_link = data['link']
            return JsonResponse({'content': yt_link})
        except (KeyError, json.JSONDecodeError):
            return JsonResponse({'error': 'Invalid request method'}, status=405)
        
        #get the title of the video


        #get transcript


        #use openai to generate the blog


        #save blog article to database


        #return blog article as response



    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

