from .models import Voter,PolledInfo,Article

from rest_framework import serializers

class VoterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Voter
        fields = ('id','name','email')

class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ('title','content','author')

class PolledInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PolledInfo
        fields = ('datetimes','ratings')