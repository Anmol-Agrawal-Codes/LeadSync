from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Lead, Agent
from .forms import LeadCreation
# Create your views here.

def home_page(request):
    lead = Lead.objects.all()
    context={
        "leads": lead
    }
    return render(request, 'leads/home_page.html', context)

def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    context = {"lead": lead}
    return render(request, 'leads/lead_details.html', context)

def create_lead(request):
    form = LeadCreation()
    if request.method == 'POST':
        Lead.objects.create(
            first_name = request.POST.get('first_name'),
            last_name = request.POST.get('last_name'),
            age = request.POST.get('age'),
            agent = Agent.objects.get(id=request.POST.get('agent'))
        )
        return redirect('home')

    context = {'form': form}
    return render(request, 'leads/create_lead.html', context)