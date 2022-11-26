import json
from urllib import response
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend
from apistage.serializers import GroupSerializer, UserSerializer ,OfferSerializer
from apistage.models import Offer
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from apistage.recomScript import recomndationSystem
from django.http import JsonResponse
from apistage import serializers
from apistage.scrapingscript import scrapingmethod
from django.http import HttpResponse
from django.core.serializers import serialize
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView
from rest_framework import status
from apistage.serializers import FileSerializer
from apistage.iapdf import run


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class OffersViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows offers to be viewed or edited.
    """
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['place', 'Keyword']





@api_view(['GET'])
def recomandation(request,profile):
    """
    recomandation profiles.
    """
    if request.method == 'GET':
        obj=recomndationSystem(profile)
        return JsonResponse(obj)

@api_view(['GET'])
def scraping(request,key):
    """
    recomandation profiles.
    """
    if request.method == 'GET':
        liste=scrapingmethod(key)
        print(liste)
        data = serialize("json", liste, fields=('title', 'companyName','Keyword','place'))
        return HttpResponse(data, content_type="application/json")

"""
class FileUploadView(APIView):
    permission_classes = []
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):

      file_serializer = FileSerializer(data=request.data)

      if file_serializer.is_valid():
          file_serializer.save()
          return Response(file_serializer.data, status=status.HTTP_201_CREATED)
      else:
          return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
          """

@api_view(['GET'])
def resume(request,file):
    """
    recomandation profiles.
    """
    if request.method == 'GET':
        jsobject=run(file)
       
        return HttpResponse(jsobject, content_type="application/json")