from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Departamentos


class DepartamentosList(ListView):
    model = Departamentos

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Departamentos.objects.filter(empresa=empresa_logada)


class DepartamentoCreate(CreateView):
    model = Departamentos
    fields = ['nome', ]

    def form_valid(self, form):
        departamento = form.save(commit=False)
        departamento.empresa = self.request.user.funcionario.empresa
        departamento.save()
        return super(DepartamentoCreate, self).form_valid(form)


class DepartamentoUpdate(UpdateView):
    model = Departamentos
    fields = ['nome']


class DepartamentoDelete(DeleteView):
    model = Departamentos
    success_url = reverse_lazy('list_departamentos')
