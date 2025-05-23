from django.shortcuts import render
from .models import Produto
from .serializers import ProdutoSerializer
from rest_framework import viewsets

# Create your views here.

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer