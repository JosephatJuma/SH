from django.shortcuts import render

def home(request):
    return render(request, "home.html", {})
def staff(request):
    return render(request, "staff-list.html", {})

