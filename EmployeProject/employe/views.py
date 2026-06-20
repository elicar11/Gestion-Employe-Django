from django.shortcuts import render
from .models import Employe


def liste_employe(request):
    employe = Employe.objects.all()
    return render(request, 'employe/index.html', {'employe': employe})