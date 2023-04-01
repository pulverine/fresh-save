from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
import datetime
from django.core.mail import send_mail,BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
import requests
from . import spoonacular
# Create your views here.

def search_recipes(request):
    query = request.GET.get('query')
    url = 'https://api.spoonacular.com/recipes/findByIngredients'
    params = {
        'apiKey': '8eca12a5acfe4b7d91fe5a6cb93fd52f',
        'ingredients': query,
        'number': 10  # Return 10 recipes
    }
    response = requests.get(url, params=params)
    recipes = response.json()
    return render(request, 'search_results.html', {'recipes': recipes})



def home(request):
    return render(request, 'home.html')

@login_required(login_url="/signup")
def loginhome(request):
    now = datetime.datetime.now()
    date_string = now.strftime("%m/%d/%y, %A")
    context = {'date_string': date_string}
    return render(request, 'lhome.html', context)

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        try:
            User.objects.get(username=request.POST['username'])
            return render(request, 'signup.html', {'error':'*Username already been taken'})
        except User.DoesNotExist:
            User.objects.create_user(username=username, password=password, email=email, )
            return redirect('login')
        # User.objects.create_user(username=username, password=password, email=email )
        # return redirect('login')
    else:
        return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('loginhome')
        else:
            return render(request, 'login.html', {'error':'*Username or password is not correct.'})

    else:
        return render(request, 'login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')