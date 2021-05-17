import random
from django.shortcuts import render, get_object_or_404, redirect
from .models import Check, Evento
from .form import CheckForm

def CheckList(request):
    checks = Check.object.filter(estado='ativo')
    return render(request, 'checklist/lista.html', {'checks': checks})

def EventoList(request):
    eventos = Evento.object.filter(nivel='basico', estado ='ativo')#.exclude(title__exact='')
    escolha = random.choice(eventos)
    return render(request, 'evento/lista.html', {'escolha': escolha})

def CheckDetalhe(request, id):
    check = get_object_or_404(Check, pk=id)
    form = CheckForm(instance=check)
    return render(request, 'checklist/detalhe.html', {'check': check,
                                                      'form': form})

def CheckEdit(request, id):
    check = get_object_or_404(Check, pk=id)
    form = CheckForm(instance=check)

    if(request.method == 'POST'):
        form = CheckForm(request.POST, instance=check)

        if(form.is_valid()):
            check.save()
            return redirect('checklist')
        else:
            return render(request, 'checklist/edita.html', {'check': check,
                                                            'form': form})
    else:
        return render(request, 'checklist/edita.html', {'check': check,
                                                    'form': form})

