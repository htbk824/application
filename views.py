from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .models import Game, Rental
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import JsonResponse

# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')  # Chuyển hướng đến trang chính sau khi đăng ký thành công
    else:
        form = UserCreationForm()
    return render(request, 'sign_up.html', {'form': form})

def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to the home page upon successful login
        else:
            # Add a message to inform the user of invalid credentials
            messages.error(request, 'Invalid username or password. Please try again.')
            return redirect('signin')  # Redirect back to the sign-in page
    else:
        return render(request, 'sign_in.html')  # Render the sign-in page for GET requests

        
def sign_out(request):
    pass

@login_required
def home(request):
    return render(request,"home.html")

def borrowed_games(request):
    games = Game.objects.all()
    return render(request,"borrowed_games.html",{'games': games})

def return_games(request):
    return render(request,"return_games.html")

def get_rental_info(request, game_name):
    try:
        rental = Rental.objects.get(game__name=game_name)
        # Kiểm tra xem có người mượn sách không
        if rental.user:
            return JsonResponse({'user': rental.user.username, 'return_date': rental.return_date.strftime('%Y-%m-%d')})
        else:
            rental_date = rental.rental_date
            return_date = rental_date + timezone.timedelta(days=14)  # Tính ngày trả sách
            return JsonResponse({'rental_date': rental_date.strftime('%Y-%m-%d'), 'return_date': return_date.strftime('%Y-%m-%d')})
    except Rental.DoesNotExist:
        return JsonResponse({'error': 'Game not found'})
    

def return_game(request):
    
    return redirect('home')



    
