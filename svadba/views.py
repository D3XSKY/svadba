from svadba.models import Proizvod, Slika, Kategorija
from svadba.serializers import ProizvodSerializer, SlikaSerializer, KategorijaSerializer
from rest_framework import generics
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, redirect
#from django.core.mail import send_mail

class ProizvodList(generics.ListCreateAPIView):
    queryset = Proizvod.objects.all()
    serializer_class = ProizvodSerializer


class ProizvodDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Proizvod.objects.all()
    serializer_class = ProizvodSerializer


class KategorijaList(generics.ListCreateAPIView):
    queryset = Kategorija.objects.all()
    serializer_class = KategorijaSerializer


class KategorijaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Kategorija.objects.all()
    serializer_class = KategorijaSerializer

class SlikaList(APIView):

    def post(self, request, format=None):
        serializer = SlikaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        photo = Slika.objects.all()
        serializer = SlikaSerializer(photo, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

class SlikaDetail(APIView):
    def get_object(self, pk):
        try:
            return Slika.objects.get(pk=pk)
        except Slika.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        photo = self.get_object(pk)
        serializer = SlikaSerializer(photo)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        photo = self.get_object(pk)
        serializer = SlikaSerializer(photo, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        photo = self.get_object(pk)
        photo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProizvodSlikaList(APIView):
    def get_slika(self, pk):
        try:
            return Slika.objects.get(pk=pk)
        except Slika.DoesNotExist:
            raise Http404
    
    def get(self, request, format=None):
        proizvodi = Proizvod.objects.all()
        serializer_p = ProizvodSerializer(proizvodi, many=True)
        data_to_return = serializer_p.data

        for i in xrange(len(proizvodi)):
            slika = self.get_slika(proizvodi[i].slika.id)
            data_to_return[i]['fajl'] = slika.fajl.url

        return Response(data_to_return)

class ProizvodSlikaDetail(APIView):
    
    def get_proizvod(self, pk):
        try:
            return Proizvod.objects.get(pk=pk)
        except Proizvod.DoesNotExist:
            raise Http404

    def get_slika(self, pk):
        try:
            return Slika.objects.get(pk=pk)
        except Slika.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        proizvod = self.get_proizvod(pk)
        slika = self.get_slika(proizvod.slika.id)
        serializer_p = ProizvodSerializer(proizvod)
        serializer_s = SlikaSerializer(slika)
        data_to_return = serializer_p.data
        data_to_return['fajl'] = slika.fajl.url
        return Response(data_to_return)

def first(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contacts.html')

def product(request):
    return render(request, 'products.html')
