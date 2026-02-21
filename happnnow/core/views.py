from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'core/home.html')

def login_view(request):
    return render(request, 'core/login.html')

def register_view(request):
    return render(request, 'core/registration.html')

def register_user(request):
    if request.method == 'POST':
        name = request.POST.get('signupName')
        email = request.POST.get('signupEmail')
        password = request.POST.get('signupPassword')
        # Create and save the user to the database
        user = User.objects.create_user(username=name, email=email, password=password)
        return redirect('login')

@login_required
def dashboard_router(request):
    if request.user.is_staff:
        return render(request, 'core/admin.html')
    else:
        return render(request, 'core/userdash.html')

@login_required
def reviews_view(request):
    return render(request, 'core/reviews.html')
