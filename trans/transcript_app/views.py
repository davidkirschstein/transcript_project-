from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import UserProfile, Grade
# Create your views here.
"""
def index(request):
    return render(request, 'myapp/index.html')
"""
def index(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember_me')

        # Authenticate user
        user = authenticate(request, username=email, password=password)

        if user is not None:
            # Login user
            login(request, user)

            # Create or get user profile
            user_profile, created = UserProfile.objects.get_or_create(user=user)

            # Additional fields can be updated here if needed
            # user_profile.birthdate = request.POST.get('birthdate')
            # user_profile.gender = request.POST.get('gender')
            # user_profile.registration_number = request.POST.get('registration_number')
            # user_profile.save()

            # Redirect to a success page or home page
            return redirect('transcript')  # Replace 'home' with your actual home page URL

    #return render(request, 'index.html')
    return render(request, '/transcript_app/index.html', {
            'title': 'index Template · Bootstrap v5.0',
            'bootstrap_css': '/transcript_app/static/transcript_app/css/bootstrap.min.css',
            'signin_css': '/transcript_app/static/transcript_app/css/signin.css',
            'bootstrap_logo': '/transcript_app/static/transcript_app/assets/brand/bootstrap-logo.svg',
    })


def registration(request):
    if request.method == 'POST':
        # Process registration form data and create User and UserProfile instances
        # ...
        return redirect('transcript')  # Replace 'transcript' with your actual transcript page URL
    return render(request, 'transcript_app/registration.html')

def transcript(request):
    # Assuming you have a logged-in user, get the UserProfile
    user_profile = UserProfile.objects.get(user=request.user)

    # Get all the grades associated with the user's profile
    grades = Grade.objects.filter(user_profile=user_profile)

    context = {
        'user_profile': user_profile,
        'grades': grades,
    }


    return render(request, 'transcript_app/transcript.html', context)

def dashboard(request):
    return render(request, 'transcript_app/dashboard.html')


