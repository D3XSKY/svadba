from rest_framework import serializers
from svadba.models import Proizvod, Slika, Kategorija#mysofraMail

class ProizvodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proizvod
        fields = ('id', 'naziv', 'slika', 'opis', 'kategorija')

class KategorijaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kategorija
        fields = ('id', 'naziv')

class SlikaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slika
        fields = ('id', 'naziv', 'fajl')

#class MailSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = mysofraMail
#        fields = ('id', 'subject', 'message', 'mail_from', 'mail_to', 'created')