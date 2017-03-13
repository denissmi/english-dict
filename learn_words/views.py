from .models import EnglishWord, RussianWord
from .serializers import EnglishWordSerializer, RussianWordSerializer, UserSerializer
from django.contrib.auth.models import User
from django.http import Http404
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView


class EnglishWordList(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        english_words = EnglishWord.objects.all()
        serializer = EnglishWordSerializer(english_words, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EnglishWordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class EnglishWordDetail(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self, pk):
        try:
            return EnglishWord.objects.get(pk=pk)
        except EnglishWord.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        english_word = self.get_object(pk)
        serializer = EnglishWordSerializer(english_word)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        english_word = self.get_object(pk)
        serializer = EnglishWordSerializer(english_word, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        english_word = self.get_object(pk)
        english_word.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RussianWordList(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        russian_words = RussianWord.objects.all()
        serializer = RussianWordSerializer(russian_words, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RussianWordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RussianWordDetail(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self, pk):
        try:
            return RussianWord.objects.get(pk=pk)
        except RussianWord.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        russian_word = self.get_object(pk)
        serializer = RussianWordSerializer(russian_word)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        russian_word = self.get_object(pk)
        serializer = RussianWordSerializer(russian_word, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        russian_word = self.get_object(pk)
        russian_word.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserList(APIView):
    def get(self, request, format=None):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
