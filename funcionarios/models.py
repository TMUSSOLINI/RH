from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models import Sum

from departamentos.models import Departamentos
from empresas.models import Empresas


class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    departamentos = models.ManyToManyField(Departamentos)
    empresa = models.ForeignKey(Empresas, on_delete=models.PROTECT, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('list_funcionarios')

    @property
    def total_horas_extra(self):
        return self.horaextra_set.all().aggregate(Sum('horas'))['horas__sum']

    def __str__(self):
        return self.nome
