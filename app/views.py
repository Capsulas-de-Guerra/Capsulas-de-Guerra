from .models import *
from django.template import Library
from rest_framework import viewsets
from .serializers import *

register = Library()


# class LojaDetail(viewsets.ModelViewSet):
#     queryset = Loja.objects.values_list('nome', 'logo__imagens')
#     serializer_class = LojaSerializer

class ExperimentViewSet(viewsets.ModelViewSet):
    queryset = Experiment.objects.all()
    serializer_class = ExperimentSerializer

    def pre_save(self, obj):
        obj.file = self.request.FILES.get('file')