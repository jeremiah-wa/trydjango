from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home_view(request, *args, **kargs):
    # return HttpResponse("<h1>Hello World</h1>")
    print(request.user)
    return render(request, "home.html", {})
