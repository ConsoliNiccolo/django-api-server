from django.shortcuts import render
from .models import Token
from rest_framework import generics
from .serializers import TokenSerializer


class TokenCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new Token
	queryset = Token.objects.all(),
	serializer_class = TokenSerializer


class TokenList(generics.ListAPIView):
    # API endpoint that allows Token to be viewed.
    queryset = Token.objects.all()
    serializer_class = TokenSerializer


class TokenDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single Token by pk.
    queryset = Token.objects.all()
    serializer_class = TokenSerializer


class TokenUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a Token record to be updated.
    queryset = Token.objects.all()
    serializer_class = TokenSerializer


class TokenDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a Token record to be deleted.
    queryset = Token.objects.all()
    serializer_class = TokenSerializer