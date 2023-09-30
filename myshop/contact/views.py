from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import FeedBack

# Create your views here.
@login_required
def contact(request):
    if request.user.is_anonymous:
        return redirect("login")
    request.session["info"]="CONTACTS"
    fbackform = FeedBack()
    if request.method == 'POST':
        fbackform = FeedBack(request.POST)
        if fbackform.is_valid():
            fbackform.save()
            return redirect('contact_page')
    return render(request, "contact.html", {"fbackform": fbackform, "page_tag": "contact_page"})

