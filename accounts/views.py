from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm

def login_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:

            login(request, user)

            if user.role == "hr":
                return redirect("hr_dashboard")

            elif user.role == "manager":
                return redirect("manager_dashboard")

            elif user.role == "worker":
                return redirect("employee_dashboard")

        return render(
            request,
            "login.html",
            {"error": "Invalid Credentials"}
        )

    return render(request, "login.html")
def hr_dashboard(request):
    return render(request, "hr_dashboard.html")


def manager_dashboard(request):
    return render(request, "manager_dashboard.html")


def employee_dashboard(request):
    return render(request, "employee_dashboard.html")
def register_view(request):

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            user.set_password(
                form.cleaned_data['password']
            )

            user.save()

            return redirect('login')

    else:
        form = RegisterForm()

    return render(
        request,
        'register.html',
        {'form': form}
    )
def home(request):
    return render(request, 'home.html')
def logout_view(request):
    logout(request)
    return redirect('home')