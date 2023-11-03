from django.shortcuts import render


from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from elrastroapp.models import Usuario
from elrastroapp.models import Producto
from elrastroapp.serializers import ProductoSerializer, UsuarioSerializer
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET', 'POST', 'DELETE'])
def usuarios_list_view(request):
    if request.method == 'GET':
        usuarios = usuario_list()
        usuarios_serializer = UsuarioSerializer(usuarios, many=True)
        return JsonResponse(usuarios_serializer.data, safe=False)    # 'safe=False' for objects serialization  

def usuario_list():
    usuarios = Usuario.objects.all()
    return usuarios

@api_view(['GET','POST','DELETE'])
def productos_list_view(request):
    if request.method == 'GET':
        productos = productos_list()
        productos_serializer = ProductoSerializer(productos, many= True)
        return JsonResponse(productos_serializer.data, safe = False)

def productos_list():
    productos = Producto.objects.all()
    return productos