from rest_framework import serializers
from .models import EnglishWord, RussianWord


class EnglishWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnglishWord
        fields = ('id', 'word', 'translation', 'rate')


class RussianWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = RussianWord
        fields = ('id', 'word', 'translation', 'rate')
