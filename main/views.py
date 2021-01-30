from django.shortcuts import render, HttpResponse

# Create your views here.
def welcome(request):
    context = {
        "hello": "world"
    }
    return render(request, 'welcome.html', context=context)

def jackpot(request):
    context = {
        "hello": "world"
    }
    return render(request, 'jackpot.html', context=context)

def register(request):
    context = {
        "hello": "world"
    }
    return render(request, 'register.html', context=context)

def lookup(request):
    context = {
        "hello": "world"
    }
    return render(request, 'lookup.html', context=context)