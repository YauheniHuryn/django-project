from django.shortcuts import render, redirect
from .forms import RegistrationForm

from django.contrib.auth.views import LoginView as BaseLoginView

# Create your views here.


def registration(request):
    rform = RegistrationForm()
    if request.method == "POST":
        rform = RegistrationForm(request.POST)
        if rform.is_valid():
            user = rform.save(commit=False)
            user.set_password(
                rform.cleaned_data["password"]
            )
            user.save()
            return redirect("login")
    return render(request, "account.html", {"rform": rform})


class LoginView:
    ...
