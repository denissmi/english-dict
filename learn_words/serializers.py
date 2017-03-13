from rest_framework import serializers
from .models import EnglishWord, RussianWord
from django.contrib.auth.models import User


class EnglishWordSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = EnglishWord
        fields = ('id', 'word', 'translation', 'rate', 'owner')


class RussianWordSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = RussianWord
        fields = ('id', 'word', 'translation', 'rate', 'owner')


class UserSerializer(serializers.ModelSerializer):
    english_words = serializers.PrimaryKeyRelatedField(many=True, queryset=EnglishWord.objects.all())
    russian_words = serializers.PrimaryKeyRelatedField(many=True, queryset=RussianWord.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'english_words', 'russian_words')