from django.db import models

# Create your models here.

#class Comerciante(models.Model):
#    name = models.CharField(max_length=200)
#    rif = models.CharField(max_length=200)

class Comerciante(models.Model):
    nombre = models.CharField(max_length=200)
    rif = models.CharField(max_length=200)
    nombre_comercio = models.CharField(max_length=200)
    correo =  models.CharField(max_length=200)
    password = models.CharField(max_length=200)


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


from django.test import TestCase
#from comercio.ps import save_pub

class PubTestCase(TestCase):
    def setUp(self):
        Publicacion.objects.create(titulo="test1")
        Publicacion.objects.create(titulo="test2")
    def test_can_add(self):
        test1 = Publicacion.objects.get(titulo="test1")
        test2 = Publicacion.objects.get(titulo="test2")
        self.assertEqual(test1.titulo, "test1")
        self.assertEqual(test2.titulo, "test2")
    def test_can_list(self):
        all = Publicacion.objects.all()
        self.assertEqual(all.count(), 2)
    '''def test_controller_add(self):
	foo = 'foo'
	saved_pub = save_pub({'titulo':foo})
        self.assertEqual(saved_pub.titulo, foo)'''

        
