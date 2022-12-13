from rest_framework import viewsets
from hora_extra.api.serializers import HoraExtraSerializer
from hora_extra.models import HoraExtra
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class HoraExtraViewSet(viewsets.ModelViewSet):
    queryset = HoraExtra.objects.all().order_by()
    serializer_class = HoraExtraSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

