from django.db import models

# Create your models here.



class Images(models.Model):

	COLOR_CHOICES = (
		('black', 'Negro'),
		('white', 'Blanco'),
		('gray', 'Gris'),
		('blue_dark', 'Azul Oscuro'),
		('blue_light', 'Azul Claro'),
		('red', 'Rojo'),
		('green', 'Verde')		
	)

	name = models.CharField(max_length=100)
	image = models.ImageField(upload_to="camisetas", null=True, blank=True)
	color = models.CharField(max_length=20, choices=COLOR_CHOICES)

	def __str__(self):
		return self.name

class Size(models.Model):
	size = models.CharField(max_length=2)

	def __str__(self):
		return self.size

class Shirt(models.Model):

	SIZE_CHOICES = (
		('s', 'S'),
		('m', 'M'),
		('l', 'L'),
		('xl', 'XL')
	)

	SEX_CHOICES = (
		('m', 'Masculino'),
		('f', 'Femenino')
	)
	TYPE_CHOICES = (
		('neck_v', 'Cuello en V'),
		('neck_round', 'Cuello Redondo')
	)
	name = models.CharField(max_length=100)
	size = models.ManyToManyField(Size)
	sex = models.CharField(max_length=2, choices=SEX_CHOICES) 
	type = models.CharField(max_length=20, choices=TYPE_CHOICES)
	price = models.FloatField()
	description = models.TextField()
	image =  models.ManyToManyField(Images)
	url = models.SlugField(max_length=80)


	def __str__(self):

		return self.name