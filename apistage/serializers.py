from django.contrib.auth.models import User, Group
from rest_framework import serializers

from apistage.models import Offer ,File


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class OfferSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Offer
        fields = ['title', 'companyName','Keyword','place']        

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"        