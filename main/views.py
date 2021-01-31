from django.shortcuts import render, HttpResponse, get_object_or_404
from .forms import CandidateForm, LookupForm, JackpotForm
from .models import Candidate
# Create your views here.
def welcome(request):
    context = {
        "hello": "world"
    }
    return render(request, 'welcome.html', context=context)

def jackpot(request,):
    message = ""
    title = ""
    if request.method == "POST":
        form = JackpotForm(request.POST)
        if form.is_valid():
            phone_number = request.POST['lookup']
            jackpot_code = request.POST['jackpot']
            
            _candidates = Candidate.objects.filter(phone_number= phone_number)
            
            if len(_candidates) == 0: 
                message = "No match candidate's phone number!"
                title = "JACKPOT"
                form = JackpotForm()
                return render(request, 'jackpot.html', {"message": message, "title": title, "form": form })
            else: 
                _candidate = _candidates[0]
                if _candidate.jackpot_keys == jackpot_code:
                    title = "CONGRATULATION!!! YOU HIT THE JACKPOT!!!"
                else: 
                    title = "SORRY!!! YOU MISS THE JACKPOT"
                return render(request, 'jackpot.html', {"title": title})
    else:
        form = JackpotForm()
        title = "JACKPOT"
        message = "    "
        return render(request, 'jackpot.html', {"message": message, "title": title, "form": form})

def register(request):
    if request.method == "POST":
        form = CandidateForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            return render(request, 'welcome.html', {"message": "New candidate added!"})
        else:
            return render(request, 'register.html', {"form": form})
    else: 
        form = CandidateForm()
        return render(request, 'register.html', {"form": form})

def lookup(request):
    context = {}
    if request.method == "POST":
        form = LookupForm(request.POST)
        if form.is_valid():
            phone_number = request.POST['lookup']
            _candidate = Candidate.objects.filter(phone_number= phone_number)
            
            if len(_candidate) == 0:
                context['message'] = "No match candidate"
            else: 
                context['message'] = "Found him/her!"
                context['match'] = _candidate[0]
            context['form'] = LookupForm()
            
            return render(request, "lookup.html", context)
        else:
            context['form'] = LookupForm()
            context['message'] = "Sai định dạng số điện thoại"
            return render(request, "lookup.html", context)
    else:
        context['form'] = LookupForm()
        return render(request, 'lookup.html', context)