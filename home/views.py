from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact, Icecream
from django.contrib import messages

# Create your views here.
def index(request):
    # context = {
      #  "variable1":"Nitesh is sent",
       # "variable2":"Puran is sent"
    #}
    # return HttpResponse("This is Home page")
    icecream = Icecream.objects.all()

    return render(request, 'index.html', {'icecream' : icecream})

def about(request):
    # return HttpResponse("This is about page")
    return render(request, 'about.html')

def services(request):
    # return HttpResponse("This is services page")
    return render(request, 'services.html')

def contact(request):
    # return HttpResponse("This is contact page")
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')
