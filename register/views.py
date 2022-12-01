from django.shortcuts import render, redirect
from .forms import RegisterForm, ProfileForm
from .models import Profile


# Create your views here.
def register(request):
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user = register_form.save()
            profile = Profile(user=user)
            profile.save()
            profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
            if profile_form.is_valid():
                profile_form.save()
        return redirect('login')

    return render(request, 'registration/register.html',
                  {'register_form': RegisterForm(), 'profile_form': ProfileForm()})
