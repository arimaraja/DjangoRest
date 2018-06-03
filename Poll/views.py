from django.shortcuts import render
from django.http import HttpResponse, Http404

from django.shortcuts import get_list_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . models import Voter, Article, PolledInfo
from . serializers import VoterSerializer, ArticleSerializer, PolledInfoSerializer


# Create your views here.
class VoterList(APIView):
    def get(self, request, format=None):
        print("VoterList");
        query = "SELECT id, name, email FROM  poll_voter";
        voters = Voter.objects.raw(query)
        serializer=VoterSerializer(voters,many=True)
        return Response(serializer.data)

    def post(self,request, format=None):
        serializer = VoterSerializer(data=request.data)
        print(serializer);
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VoterListDetails(APIView):

    def get_object(self,pk):
        print("VoterDetailList")
        try:
            return Voter.objects.get(pk=pk)
        except Voter.DoesNotExist:
            raise Http404

    def get(self, request,pk, format=None):
        query = self.get_object(pk)
        print (request.data)
        serializer=VoterSerializer(query)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = VoterSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

""""
    def post(self,request,format=None):
        serializer = VoterSerializer(data=request.data)
        print(serializer.data);
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""

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
