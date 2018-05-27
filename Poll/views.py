from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import get_list_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . models import Voter, Article, PolledInfo
from . serializers import VoterSerializer, ArticleSerializer, PolledInfoSerializer


# Create your views here.

class VoterList(APIView):
    def get(self, request):
        voters = Voter.objects.all()
        serializer=VoterSerializer(voters,many=True)
        return Response(serializer.data)

    def post(self,request):
        pass

class ArticleList(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer=ArticleSerializer(articles,many=True)
        return Response(serializer.data)

    def post(self,request):
        pass

class PolledInfoList(APIView):
    def get(self, request):
        pollinfos = PolledInfo.objects.all()
        serializer=PolledInfoSerializer(pollinfos,many=True, context={'request':request})
        return Response(serializer.data)

    def post(self,request):
        pass

def index(request):
    return HttpResponse("Hello, world Your polling index");
