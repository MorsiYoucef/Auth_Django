from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout



# Create your views here.
@login_required
def home(request):
    return render(request, "home.html", {})

def authView(request):
    form = UserCreationForm(request.POST or None)  # Initialize form for both GET and POST

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect("base:login")  # Redirect to login page after successful registration

    # Render the form whether it’s a GET request or an invalid POST request
    return render(request, "registration/signup.html", {"form": form})


def logout_view(request):
    logout(request)
# def authView(request):
#     form = UserCreationForm()
#     return render(request, "registration/signup.html", {"form": form})
