from rest_framework import serializers
from funcionarios.models import Funcionario
from hora_extra.api.serializers import HoraExtraSerializer


class FuncionarioSerializer(serializers.ModelSerializer):
    horaextra_set= HoraExtraSerializer(many=True)
    class Meta:
        model = Funcionario
        fields = ('id','nome', 'user', 'departamentos', 'empresa','imagem',
                  'total_horas_extra', 'horaextra_set')
