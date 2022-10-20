from django.shortcuts import render
import datetime
from .models import Transacao
from .form import TransacaoForm


def home(request):
    data = {}
    data['now'] = datetime.datetime.now()
    return render(request, 'contas/home.html', data)

def listagem(request):
    data = {}
    data['transacoes'] = Transacao.objects.all()
    return render(request, 'contas/listagem.html', data)

def nova_transacao(request):
    form = TransacaoForm(request.POST or None)
    return render(request, 'contas/form.html', {'form': form})

def update(request):
    data = {}
    transacao = Transacao.objects.filter(pk=pk)
    form = TransacaoForm(request.POST or None, instance=transacao)
    data['form'] = form
    return render(request, 'contas/form.html', data)
