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
		return "%s - %s" % (self.name, self.color)

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
	price = models.IntegerField()
	description = models.TextField()
	image =  models.ManyToManyField(Images)
	slug = models.SlugField(max_length=80)


	def __str__(self):

		return self.name



class ShirtOrder(models.Model):

	COLOR_CHOICES = (
		('black', 'Negro'),
		('white', 'Blanco'),
		('gray', 'Gris'),
		('blue_dark', 'Azul Oscuro'),
		('blue_light', 'Azul Claro'),
		('red', 'Rojo'),
		('green', 'Verde')		
	)

	shirt = models.ForeignKey(Shirt, on_delete=models.CASCADE)
	color = models.CharField(max_length=20, choices=COLOR_CHOICES)
	quantity = models.IntegerField(default=1)


	def __str__(self):

		return "%s - %s - %s" % (self.shirt.name, self.color, self.quantity)

class Order(models.Model):


	STATUS_CHOICES = (
		('paid', 'Pagado'),
		('received', 'Recibido'),
		('in-process', 'En Proceso'),
		('cancel', 'Cancelado'),
		('sent', 'Enviado')
	)

	name = models.CharField(max_length=100)
	phone = models.CharField(max_length=100)
	email = models.EmailField(max_length=100)
	status = models.CharField(max_length=20, choices=STATUS_CHOICES)
	product = models.ManyToManyField(ShirtOrder)
	total = models.IntegerField()
	iva = models.CharField(max_length=10, default='0')
	number = models.IntegerField(unique=True)
	delivery_date = models.DateField()
	address = models.CharField(max_length=200)


	def __str__(self):

		return self.name



