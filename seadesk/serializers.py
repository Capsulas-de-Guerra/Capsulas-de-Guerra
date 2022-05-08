from rest_framework import serializers
from .models import *

# class LojaSerializer(serializers.ModelSerializer):
#     class Meta:

#         model = Loja
#         depth = 1
#         fields = "__all__"

# class EnderecoSerializer(serializers.ModelSerializer):
#     class Meta:

#         model = Endereco
#         fields =models.TextField(blank=True)

class ExperimentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experiment
        fields =  "__all__"