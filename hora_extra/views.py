from django.shortcuts import render
from django.views.generic import ListView
from .models import HoraExtra


class HoraExtraList(ListView):
    model = HoraExtra

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return HoraExtra.objects.filter(funcionario__empresa= empresa_logada)
