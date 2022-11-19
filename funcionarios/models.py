from django.db import models
from django.contrib.auth.models import User
from departamentos.models import Departamentos
from empresas.models import Empresas


class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    departamentos = models.ManyToManyField(Departamentos)
    empresa = models.ForeignKey(Empresas, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.nome
