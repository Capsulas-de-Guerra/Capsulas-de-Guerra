from io import TextIOBase
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


class EnvioImagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnvioImagem
        fields =  "__all__"

class EnvioRelatorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnvioRelatorio

        fields =  "__all__"



class CaixaRelatorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caixa

        fields =  "__all__"



class LogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logs

        fields =  "__all__"


        