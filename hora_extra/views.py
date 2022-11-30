from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import RegistroHoraExtraForm
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import HoraExtra


class HoraExtraList(ListView):
    model = HoraExtra

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return HoraExtra.objects.filter(funcionario__empresa= empresa_logada)


class HoraExtraEdit(UpdateView):
    model = HoraExtra
    form_class = RegistroHoraExtraForm

    def get_form_kwargs(self):
        kwargs = super(HoraExtraEdit, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class HoraExtraDelete(DeleteView):
    model = HoraExtra
    success_url = reverse_lazy('list_hora_extra')

class HoraExtraNovo(CreateView):
    model = HoraExtra
    form_class = RegistroHoraExtraForm

    def get_form_kwargs(self):
        kwargs = super(HoraExtraNovo, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs
