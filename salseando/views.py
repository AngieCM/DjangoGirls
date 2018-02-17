from django.shortcuts import render
from salseando.models import gruposalsa

# Create your views here.

def grupos(request):
    return render (request, 'grupos.html', {
        'grupos': gruposalsa.objects.all(),
        'titulo': 'Me dan ganas de bailar',
    })
