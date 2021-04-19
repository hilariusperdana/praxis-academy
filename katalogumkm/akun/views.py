from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import SignUpForm
from akun.models import Profile


def Register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Akun baru telah berhasil dibuat, dengan username: {username}!')
            password = form.cleaned_data.get('password1')
            return redirect("/")

        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

            return render(request=request,
                          template_name="accounts/auth/register.html",
                          context={"form": form})

    form = SignUpForm
    return render(request=request,
                  template_name="accounts/auth/register.html",
                  context={"form": form})