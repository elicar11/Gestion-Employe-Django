from django.shortcuts import render, redirect, get_object_or_404
from .models import Employe
from .forms import EmployeForm


def liste_employe(request):
    employe = Employe.objects.all()
    return render(request, 'employe/index.html', {'employe': employe})

def ajouter_employe(request):
    forms = EmployeForm(request.POST or None)
    if forms.is_valid():
        forms.save()
        return redirect('liste_employe')
    return render(request,'employe/formulaire.html', {'forms': forms})

def modifier_employe(request, id):
    employe = get_object_or_404(Employe, id=id)
    forms = EmployeForm(request.POST or None , instance=employe)
    if forms.is_valid():
        forms.save()
        return redirect('liste_employe')
    return render(request, 'employe/formulaire.html', {'forms': forms})

def supprimer_employe(request, id):
    employe = get_object_or_404(Employe, id=id)
    if request.method == 'POST':
        employe.delete()
        return redirect('liste_employe')
    return render(request, 'employe/supprimer.html', {'employe': employe})