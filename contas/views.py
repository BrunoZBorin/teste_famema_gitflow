from django.shortcuts import render
import datetime
from .models import Transacao
from .form import TransacaoForm


def home(request):
    data = {}
    return render(request, 'contas/home.html', data)

def listagem(request):
    data = {}
    data['transacoes'] = Transacao.objects.all()
    return render(request, 'contas/listagem.html', data)

def nova_transacao(request):
    data = {}
    form = TransacaoForm()
    data['form'] = form
    return render(request, 'contas/form.html', data)
