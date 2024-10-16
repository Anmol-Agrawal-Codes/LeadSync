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
        form = LeadCreation(request.POST)
        if(form.is_valid()):
            lead_data = form.cleaned_data
            Lead.objects.create(
                first_name = lead_data.get('first_name'),
                last_name = lead_data.get('last_name'),
                age = lead_data.get('age'),
                agent = lead_data.get('agent')
            )
        return redirect('home')

    context = {'form': form}
    return render(request, 'leads/create_lead.html', context)

def update_lead(request, pk):
    lead = Lead.objects.get(id=pk)
    form = LeadCreation(instance=lead)
    if request.method == 'POST':
        form = LeadCreation(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect('lead-details', pk)
    context = {'form': form}
    return render(request, 'leads/update_lead.html', context)

def delete_lead(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect('home')