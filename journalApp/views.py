from django.shortcuts import render
from .models import *
from django.db.models import Q

def index(request):
    title = request.GET.get('title') if request.GET.get('title') != None else ''
    author = request.GET.get('author') if request.GET.get('author') != None else ''
    journal = request.GET.get('journal') if request.GET.get('journal') != None else ''
    
    # Without adding Q that means the search parameter has to match everything
    papers = Paper.objects.filter(Q(title__icontains=title, author__icontains=author, journal__name__icontains=journal)).order_by('-id')[:6]
    
    journals = Journal.objects.all()

    context = {'journals':journals, 'papers':papers}
    return render(request, 'journalApp/index.html', context)

def journal(request, pk):
    journal = Journal.objects.get(id=pk)
    papers = journal.paper_set.all().order_by('-id')
    volumes = journal.volume_set.all()
    context = {'journal':journal,'papers':papers,'volumes':volumes}
    return render(request, 'journalApp/journal_page.html', context)

def volume(request, pk):
    volume = Volume.objects.get(id=pk)
    issues = volume.issue_set.all()
    context = {'journal':journal, 'volume':volume,'issues':issues}
    return render(request, 'journalApp/volume_page.html', context)

def paper_view(request, pk):
    paper = Paper.objects.get(id=pk)
    context = {'paper':paper}
    return render(request, 'journalApp/paper.html', context)