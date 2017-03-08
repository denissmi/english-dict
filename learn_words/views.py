from rest_framework.views import APIView
from .models import EnglishWord, RussianWord
from .serializers import EnglishWordSerializer, RussianWordSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


class EnglishWordList(APIView):
    def get(self, request, format=None):
        snippets = EnglishWord.objects.all()
        serializer = EnglishWordSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EnglishWordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EnglishWordDetail(APIView):
    def get_object(self, pk):
        try:
            return EnglishWord.objects.get(pk=pk)
        except EnglishWord.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = EnglishWordSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = EnglishWordSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RussianWordList(APIView):
    def get(self, request, format=None):
        snippets = RussianWord.objects.all()
        serializer = RussianWordSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RussianWordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RussianWordDetail(APIView):
    def get_object(self, pk):
        try:
            return RussianWord.objects.get(pk=pk)
        except RussianWord.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = RussianWordSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = RussianWordSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
