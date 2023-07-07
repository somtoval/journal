from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q
from django.contrib import messages

def index(request):
    title = request.GET.get('title') if request.GET.get('title') != None else ''
    author = request.GET.get('author') if request.GET.get('author') != None else ''
    journal = request.GET.get('journal') if request.GET.get('journal') != None else ''
    
    print('title: ', title, 'author:', author, 'journal:', journal)
    # Without adding Q that means the search parameter has to match everything
    papers = Paper.objects.filter(Q(title__icontains=title) & Q(author__icontains=author) & Q(journal__name__contains=journal)).order_by('-id')[:6]
    
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

def issue_page(request, pk):
    issue = Issue.objects.get(id=pk)
    papers = issue.paper_set.all()
    paper_count = papers.count()
    context = {'issue':issue, 'papers':papers, 'paper_count':paper_count}
    return render(request, 'journalApp/issue_page.html', context)

def submit(request):
    # print('printing...1', request.POST)
    # print('printing...2', request.FILES)
    # print('printing...3', request.FILES.keys())
    # # print('printing...3', request.FILES["fileUpload"])
    # # print('printing...5', list(request.FILES.keys()))
    # # thelist = list(request.FILES.keys())
    # # print(request.FILES[thelist[0]])
    # # print('printing...5', request.FILES[list(request.FILES.keys())[0]])

    # firstname = request.POST.get('firstname')
    # lastname = request.POST.get('lastname')
    # email = request.POST.get('email')
    # email_confirm = request.POST.get('email_confirm')
    # phonenumber = request.POST.get('phonenumber')
    # institution = request.POST.get('institution')
    # country = request.POST.get('country')
    # fileUpload = request.FILES['fileUpload']
    # fileUpload2 = request.FILES['fileUpload2']

    # print(firstname, lastname, email, email_confirm, phonenumber, institution, country, fileUpload, fileUpload2)

    if request.method == 'POST':
        journalid = request.POST.get('journalId')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        email_confirm = request.POST.get('email_confirm')
        phonenumber = request.POST.get('phonenumber')
        institution = request.POST.get('institution')
        country = request.POST.get('country')
        journalname = Journal.objects.get(id=journalid)
        if request.FILES != None:
            fileUpload = request.FILES.get('fileUpload')
            fileUpload2 = request.FILES.get('fileUpload2')
            print(journalname, firstname, lastname, email, email_confirm, phonenumber, institution, country, fileUpload, fileUpload2)
        else:
            print('Everybody it is empty oooh')

        if email == email_confirm:
            if fileUpload and fileUpload.size < 10 * 1024 * 1024:  # 10 MB limit
                if fileUpload2 and fileUpload2.size < 10 * 1024 * 1024:  # 10 MB limit
                    Submission.objects.create(journal=journalname, firstname=firstname, lastname=lastname, email=email, phonenumber=phonenumber, institution=institution, country=country, manuscript=fileUpload, supplementary=fileUpload2)
                    messages.success(request, 'Your Submission has been recieved')
                    return redirect('home')
                else:
                    messages.error(request, 'Your Supplementary file exceeds limit!')
                    print('Supplementary File exceeds limit')
            else:
                messages.error(request, 'Your File exceeds limit!')
                print('File exceeds limit')
        else:
            messages.error(request, 'Your email fields does not match!')
            print('Email fields do not match')
    
        # btnUpload = request.FILES.get('btnUpload')
        # btnUpload2 = request.FILES.get('btnUpload2')

        print(firstname, lastname, email, email_confirm, phonenumber, institution, country, fileUpload, fileUpload2)
    

    journals = Journal.objects.all()
    context = {'journals':journals}
    return render(request, 'journalApp/submit.html', context)

def all_journals(request):
    journals = Journal.objects.all()
    journal_count = journals.count()
    context = {'journals':journals, 'journal_count':journal_count}
    return render(request, 'journalApp/active-journals.html', context)

def topics(request):
    context = {}
    return render(request, 'journalApp/topics.html', context)

def about(request):
    context = {}
    return render(request, 'journalApp/about.html', context)

def contact(request):
    context = {}
    return render(request, 'journalApp/contact-us.html', context)

def authors(request):
    context = {}
    return render(request, 'journalApp/authors.html', context)

def reviewers(request):
    context = {}
    return render(request, 'journalApp/reviewers.html', context)

def editors(request):
    context = {}
    return render(request, 'journalApp/editors.html', context)

def openAccessPolicy(request):
    context = {}
    return render(request, 'journalApp/open-access.html', context)

def editorialProcess(request):
    context = {}
    return render(request, 'journalApp/editorial-process.html', context)

def ethics(request):
    context = {}
    return render(request, 'journalApp/research-and-publication-ethics.html', context)

def charges(request):
    context = {}
    return render(request, 'journalApp/article-processing-charges.html', context)