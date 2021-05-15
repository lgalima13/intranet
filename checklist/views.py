from django.shortcuts import render
from .models import Check

def CheckList(request):
    checks = Check.object.filter(estado='ativo')
    return render(request, 'checklist/lista.html', {'checks': checks})