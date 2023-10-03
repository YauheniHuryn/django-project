from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import FeedBackForm

# Create your views here.

def contact(request):
    fbackform = FeedBackForm()
    if request.method == 'POST':
        fbackform = FeedBackForm(request.POST)
        if fbackform.is_valid():
            fbackform.save()
            return redirect('contact_page')
    return render(request, "contact.html", {"fbackform": fbackform, "page_tag": "contact_page"})

