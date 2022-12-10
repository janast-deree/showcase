from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest, HttpResponseForbidden
from django.shortcuts import render, redirect
from .forms import RegisterForm, ProfileForm, UserUpdateForm
from .models import Profile


# Create your views here.
def register(request):
    if request.user.is_authenticated:
        return HttpResponseForbidden()
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        if not register_form.is_valid():
            return HttpResponseBadRequest
        user = register_form.save()
        user_profile = Profile(user=user)
        user_profile.save()
        profile_form = ProfileForm(request.POST, request.FILES, instance=user_profile)
        if profile_form.is_valid():
            profile_form.save()
        login(request, user)
        return redirect('home')

    return render(request, 'registration/register.html',
                  {'register_form': RegisterForm(), 'profile_form': ProfileForm()})


@login_required
def profile(request):
    user = request.user
    if user.is_superuser:
        return redirect('admin:index')
    user_profile = request.user.profile
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=user_profile)
        if not user_form.is_valid() or not profile_form.is_valid():
            return HttpResponseBadRequest()
        user_form.save()
        profile_form.save()
    return render(request, 'registration/profile.html',
                  {'user_form': UserUpdateForm(instance=user),
                   'profile_form': ProfileForm(instance=user_profile)})
