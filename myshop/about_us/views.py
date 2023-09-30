from django.shortcuts import render

def about(request):
    return render(request, "about.html", {"page_tag": "about_page"})
