from django.shortcuts import render
from django.views.generic import ListView, UpdateView
from .models import HoraExtra


class HoraExtraList(ListView):
    model = HoraExtra

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return HoraExtra.objects.filter(funcionario__empresa= empresa_logada)

class HoraExtraEdit(UpdateView):
    model = HoraExtra
    fields = ['motivo', 'funcionario', 'horas']
