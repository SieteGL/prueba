from django.db import models

class Empresa(models.Model):

    COUNTRY = (
        ('0','ARGENTINA'),
        ('1','BOLIVIA'),
        ('2','PARAGUAY'),
        ('3','CHILE'),
        ('4','COLOMBIA'),
        ('5','PERÚ'),
        ('6','URUGUAY'),
        ('7','ECUADOR'),
        ('8','MÉXICO'),
        ('9','VENEZUELA'),
    )

    AREA = (
        ('0','+54'),
        ('1','+591'),
        ('2','+595'),
        ('3','+56'),
        ('4',''),
        ('5',''),
        ('6',''),
        ('7',''),
        ('8',''),
        ('9',''),
    )

    nombre_empresa = models.TextField(
        'Nombre de la empresa',
        blank=True
    )

    rut = models.TextField(
        'Rut Empresa',
        blank = True 
    )

    pais = models.CharField(
        'País',
        max_length=2,
        choices=COUNTRY,
        blank=True
    )
    
    codigo_area = models.CharField(
        'Codigo area país',
        choice=AREA,
        blank=True
    )

    año_fundacion = models.DateTimeField(
        'Fecha de fundacion',
        blank=True,
        null=True
    )

    representante = models.TextField(
        'Nombre representante',
        blank=True
    )

    region = models.TextField(
        'Region',
        blank=True
    )

    comuna = models.TextField(
        'Comuna',
        blank=True
    )

    calle = models.TextField(
        'calle',
        blank=True
    )
