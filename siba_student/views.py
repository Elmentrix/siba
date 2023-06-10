from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .forms import student_form


# Create your views here.
def home(request):
    return render(request, "home.html")

def application(request):
    form = student_form()

    # checking for post method and validation
    if request.method == "POST":
        form = student_form(request.POST)
        if form.is_valid:
            form.save()
            return redirect('home')
    else:
        form = student_form()

    context = {
        'form': form
    }

    return render(request, "application.html", context)