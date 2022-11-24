from django.db import models
from empresas.models import Empresas


class Departamentos(models.Model):
    nome = models.CharField(max_length=70)
    empresa = models.ForeignKey(Empresas, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome
