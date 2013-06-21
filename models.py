from django.db import models
#------------------------------------------
class Genero(models.Model):
	sexo	= models.CharField(max_length=10, primary_key=True, null=False)
	descr	= models.CharField(max_length=25, null=False)

	class Meta:
		db_table='genero'
#------------------------------------------
class Marital(models.Model):
	estado_civil	= models.CharField(max_length=25, null=False, primary_key=True)
	descr			= models.CharField(max_length=25, null=False)

	class Meta:
		db_table='marital'
#------------------------------------------
class Nacionalidad(models.Model):
	abbr_estado		= models.CharField(max_length=5, primary_key=True, null=False)
	descr			= models.CharField(max_length=100)	
	nacimiento		= models.CharField(max_length=50)
	clave_estado	= models.IntegerField()

	class Meta:
		db_table='nacionalidad'
#------------------------------------------
class Personal(models.Model):
	rfc			= models.CharField(max_length=13, primary_key=True, null=False)
	apellidop 	= models.CharField(max_length=50, null=False)
	apellidom	= models.CharField(max_length=50, blank=True)
	nombre		= models.CharField(max_length=100, null=False)
	curp		= models.CharField(max_length=18, null=False, unique=True)
	sexo		= models.ForeignKey(Genero)
	estado_civil= models.ForeignKey(Marital)
	abbr_estado	= models.ForeignKey(Nacionalidad)
	ingreso_gob	= models.DateField(auto_now_add=False, null=False)
	ingreso_dep	= models.DateField(auto_now_add=False, null=False)
	domicilio	= models.CharField(max_length=200, blank=True, null=True)
	colonia		= models.CharField(max_length=200, blank=True, null=True)
	municipio	= models.CharField(max_length=200, blank=True, null=True)
	cedula		= models.BigIntegerField(default=0)

	class Meta:
		db_table='personal'
		
#------------------------------------------
class Programa(models.Model):
	tipo_trabajador	= models.CharField(max_length=25, primary_key=True)
	descr			= models.CharField(max_length=50, null=False)

	class Meta:
		db_table='programa'
#------------------------------------------
class Autoridad(models.Model):
	autoridad		= models.CharField(max_length=25, null=False, primary_key=True)
	descr			= models.CharField(max_length=50, blank=True)

	class Meta:
		db_table='autoridad'
		
#------------------------------------------
class Codigo(models.Model):
	codigo		= models.CharField(max_length=10, primary_key=True, unique_for_date='anio')
	descr		= models.CharField(max_length=50)
	rama		= models.CharField(max_length=25)
	partida_02	= models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
	partida_42	= models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
	partida_55	= models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
	anio		= models.DateField(auto_now_add=False)

	class Meta:
		db_table='codigo'
#------------------------------------------
class Adscripcion(models.Model):
	cr 			= models.IntegerField(primary_key=True)
	descr		= models.CharField(max_length=150)
	jnum		= models.SmallIntegerField()
	fisicamente	= models.IntegerField()
	fdescr		= models.CharField(max_length=150)
	
	class Meta:
		db_table='adscripcion'
#------------------------------------------
class Tipot(models.Model):
	tipo		= models.CharField(max_length=10, primary_key=True)
	descr		= models.CharField(max_length=25)

	class Meta:
		db_table='tipot'
#------------------------------------------
class Plantilla(models.Model):
	rfc				= models.CharField(max_length=13, null=False)
	vigencia_del	= models.DateField(auto_now_add=False, null=False)
	vigencia_al		= models.DateField(auto_now_add=False, null=False)
	cr				= models.ForeignKey(Adscripcion)
	autoridad		= models.ForeignKey(Autoridad)
	activo			= models.BooleanField(default=True)
	tabulador		= models.SmallIntegerField()
	jornada			= models.SmallIntegerField()
	tipo_trabajador	= models.ForeignKey(Programa)
	tipot			= models.ForeignKey(Tipot)
	clave_presupuestal = models.CharField(max_length=30, null=False)
	fakerfc			= models.CharField(max_length=13)
	codigo			= models.ForeignKey(Codigo)
	anio			= models.SmallIntegerField()
	quincena		= models.SmallIntegerField()

	class Meta:
		db_table='plantilla'
	
#------------------------------------------

#------------------------------------------

		
