from typing import overload
from urllib import request
from django.shortcuts import get_object_or_404, render
from landing.models import BlogPost, Landing, Servicos
from .models import *
from ipware import get_client_ip
from django.template import Library
from rest_framework import viewsets
from .serializers import *
import base64
from PIL import Image
import io


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User

class FindCaixa(viewsets.ViewSet):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    serializers = CaixaRelatorioSerializer
    authentication_classes = [authentication.TokenAuthentication]


    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        caixas = [Caixa.nome for nome in Caixa.objects.all()]
        return Response(caixas)  
    
    def post(self, request, format=None):
        """
        Return a list of all users.
        """
        caixas = [Caixa.nome for nome in Caixa.objects.filter(nome=request.data.busca)]
        return Response(caixas)



def vue_test(request):
    return render(request, 'landing/index.html')

def visitante(request):
    ip, is_routable = get_client_ip(request)
    if ip is None:
        visita = Visitante(ip='None', path = request.path, info = request.path_info)
        visita.save()
    else:
        
        if is_routable:
            visita = Visitante(ip=ip, path = request.path, info = request.path_info)
            visita.save()
        else:
            visita = Visitante(ip='Private', path = request.path, info = request.path_info)
            visita.save()


def index(request):
    visitante(request)
    services = Servicos.objects.all()
    carrocel = Carrocel.objects.all()
    landing = get_object_or_404(Landing, id=1)
    ##images = Envio.objects.all()
    ##lista = []
    ##for image in images:
    ##    temp =  image.imagem
    ##    img = Image.open(io.BytesIO(base64.decodebytes(bytes(temp, "utf-8"))))
    ##    img.save(image.nome)
    content  = {
        'services': services,
        'landing': landing,
        'title':landing.title,
        'carrocel':carrocel,
        

    }
    return render(request, 'landing/landing.html', content)
 



def servicos(request, path):
    visitante(request)
    services = Servicos.objects.all()
 

    for servico in services:
        content  = {
            'services': services,
            'title':servico.nome,
            'servico':servico,
  
        }
        if servico.url == path:

            return  render(request, 'landing/servicos.html', content)
      
    content  = {
        'services': services,
        'title':'Página não encontrada',
        
    }      
    return render(request, 'landing/404.html', content)

def blog(request):
    visitante(request)
    return render(request, 'landing/blog.html')


def blogPost(request, id):
    visitante(request)
    post = get_object_or_404(BlogPost, id = id)
    services = Servicos.objects.all()
    content  = {
        'services': services,
        'post': post,
        'title':post.title,

    }
    return render(request, 'landing/blogPost.html', content)

