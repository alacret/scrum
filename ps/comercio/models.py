from django.db import models

# Create your models here.

#class Comerciante(models.Model):
#    name = models.CharField(max_length=200)
#    rif = models.CharField(max_length=200)

class Publicacion(models.Model):
     titulo = models.CharField(max_length=200)
     productos = models.TextField()
     direccion = models.CharField(max_length=200)
     nombre_comercio = models.CharField(max_length=200)
     nombre_comerciante = models.CharField(max_length=200)
#    poll = models.ForeignKey(Comerciante)
#    choice_text = models.CharField(max_length=200)
#    votes = models.IntegerField(default=0)
     pub_date = models.DateTimeField(auto_now_add=True)


import unittest 

class PubAddTestCase(unittest.TestCase):
    def testAdd(self):
	test_string = "titulo de prueba"
	pub = Publicacion()
	pub.titulo = test_string
	pub.save()
        self.assertEqual(pub.titulo, test_string)
