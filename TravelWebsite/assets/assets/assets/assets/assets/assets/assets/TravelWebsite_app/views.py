from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def reservation(request):
    return render(request, 'reservation.html')

def deals(request):
    return render(request, 'deals.html')

