from django.shortcuts import render
from myapp.models import Presidente

# Create your views here.
def list_presidentes(request):
    presidentes = Presidente.objects.all()
    context = {
        "presidentes": presidentes
    }
    return render(request, 'myapp/list-presidentes.html', context)

def detail_presidentes(request, id):
    presidente = Presidente.objects.filter(numero=id).first()
    context = {
        "presidente": presidente
    }
    return render(request, 'myapp/detail-presidentes.html', context)

def home(request):
    context = {
        
    }
    return render(request, 'myapp/home.html', context)