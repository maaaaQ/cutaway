from django.shortcuts import redirect, render
from .forms import RegForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def registration(request):
    if request.method == "POST":
        form = RegForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request, f"Пользователь {username} был успешно зарегистрирован"
            )
            return redirect("home")
    else:
        form = RegForm()
    return render(
        request,
        "reg/registration.html",
        {
            "title": "Регистрация",
            "form": form,
        },
    )


@login_required
def profile(request):
    return render(request, "reg/profile.html")
