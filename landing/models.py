from io import TextIOWrapper
from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.db.models.base import Model
from django.db.models.deletion import CASCADE, DO_NOTHING
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import ForeignKey, ManyToManyField
from django.db.models.query_utils import PathInfo
# Create your models here.



class Upload(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField()

class Imagem(models.Model):
	imagem = models.ImageField(upload_to='images/', blank=True,null=True)	

class Landing(models.Model):
    title = models.CharField(max_length=50)
    mensagemFlayer1 = models.CharField(max_length=250)
    mensagemFlayer2 = models.CharField(max_length=250)
    imagem = models.ForeignKey(Imagem, on_delete=models.DO_NOTHING)
    def ___str___(self):
        return  self.title

class Carrocel(models.Model):
    nome = models.CharField(max_length=50)
    imagem = models.CharField(max_length=250)
    def ___str___(self):
        return  self.nome

class Descricao(models.Model):
    descricao = models.CharField(max_length=500)
    def ___str___(self):
        return  self.descricao

class Tag(models.Model):
    tag = models.CharField(max_length=50)
    def ___str___(self):
        return  self.tag


class Card(models.Model):
    icon = models.CharField(max_length=30)
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=500)
    def ___str___(self):
        return  self.nome

class Opcoes(models.Model):
    opcao = models.CharField(max_length=50)
    def ___str___(self):
        return  self.opcao

class Precos(models.Model):
    tipo = models.CharField(max_length=50)
    valorMensal = models.FloatField()
    valorAnual = models.FloatField()
    opcoes = models.ManyToManyField(Opcoes, null=True, blank= True)
    extra = models.CharField(max_length=100)
    def ___str___(self):
        return  self.tipo

class Precos_Services(models.Model):
    nome = models.CharField(max_length=500)
    inicial = models.FloatField()
    descricoes = models.ForeignKey(Descricao, on_delete=DO_NOTHING)
    preco = models.ManyToManyField(Precos, null=True, blank=True)
    def ___str___(self):
        return  self.nome

class Servicos(models.Model):
    url = models.CharField(max_length=20)
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=500)
    icon = models.CharField(max_length=30)
    imagem = models.CharField(max_length=250, null=True, blank=True)
    card =  models.ManyToManyField(Card,  null=True, blank= True)
    texto = models.CharField(max_length=5000)
    tag = models.ForeignKey(Tag, on_delete=DO_NOTHING, null=True, blank= True)
    precos_servico = ManyToManyField(Precos, blank= True, null= True)
    def ___str___(self):
        return  self.nome

class BlogPost(models.Model):
    imagem = models.CharField(max_length=250)
    title = models.CharField(max_length=5000)
    texto1 = models.CharField(max_length=5000)
    textoDestaque = models.CharField(max_length=5000)
    textoConclusao = models.CharField(max_length=5000)
    tags = ManyToManyField(Tag, blank= True, null= True)
    dataPost = models.DateField(blank=True, null=True)
    autor = models.ForeignKey(User, on_delete=DO_NOTHING, blank=True, null=True)
    def ___str___(self):
        return  self.title 

class Visitante(models.Model):
    ip = models.CharField(max_length=150)
    path = models.CharField(max_length=150)
    info = models.CharField(max_length=500)
    def ___str___(self):
        return  self.ip 


class Caixa(models.Model):
    nome = models.CharField(max_length=500)  


class EnvioImagem(models.Model):
    nome = models.CharField(max_length=500, blank=True, null=True)
    hash = models.CharField(max_length=500, blank=True, null=True)
    dir = models.CharField(max_length=500, blank=True, null=True)
    pagina = models.IntegerField(blank=True, null=True)
    caixa = models.CharField(max_length=500, blank=True, null=True)
    imagem = models.TextField(blank=True, null=True)

class EnvioRelatorio(models.Model):
    username = models.CharField(max_length=500)
    dataHora = models.DateTimeField()
    documentoDigitalizado = models.IntegerField()


class Logs(models.Model):
    log = models.CharField(max_length=5000)
    

 