from django.db import models


class Slika(models.Model):
    naziv = models.CharField(max_length=255)
    fajl = models.ImageField(upload_to='slike/', null=True, max_length=255)
    
    def __str__(self):
    	return str(self.naziv);

class Kategorija(models.Model):
	naziv = models.CharField(max_length=255)

	def __str__(self):
		return str(self.naziv);
		
class Proizvod(models.Model):
    naziv = models.CharField(max_length=100, blank=True, default='')
    slika = models.ForeignKey(Slika, on_delete=models.CASCADE)
    opis = models.CharField(max_length=2000, blank=True, default='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc eget mollis urna, imperdiet malesuada eros. Nunc eget mollis urna, imperdiet malesuada eros.')
    kategorija = models.ForeignKey(Kategorija)

    def __str__(self):
    	return str(self.naziv);

#class mysofraMail(models.Model):
#    created = models.DateTimeField(auto_now_add=True)
#    subject = models.CharField(max_length=100, blank=True, default='')
#    message = models.TextField()
#    mail_from = models.CharField(default='checkouts@mysofra.at', max_length=100)
#    mail_to = models.CharField(default='orders@mysofra.at', max_length=100)

#    class Meta:
#        ordering = ('created',)