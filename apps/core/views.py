from django.shortcuts import render

# Create your views here.
def frontpage(request):
    return render(request, 'frontpage.html')

def contactpage(request):
    return render(request, 'contact.html')