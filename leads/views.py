from django.shortcuts import render
from django.http import HttpResponse
from .models import Lead
# Create your views here.

def home_page(request):
    # return HttpResponse("hello world")
    lead = Lead.objects.all()
    context={
        "leads": lead
    }
    return render(request, "leads/home_page.html", context)