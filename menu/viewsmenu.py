from django.shortcuts import render

# Create your views here.
def menu(request):
    return render(request, 'menu.html')

def graficas2(request):
    return render(request, 'coming_soon.html')
