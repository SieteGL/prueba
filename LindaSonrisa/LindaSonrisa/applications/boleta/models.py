from django.db import models

class Boleta(models.Model):

    valor_unitario = models.PositiveIntegerField("Valor por unidad")

    cantidad = models.PositiveIntegerField("Cantidad de productos")

    valor_total = models.PositiveIntegerField("Valor total productos")


    fecha_atencion = models.DateTimeField(
        'Fecha de atencion',
        blank=True,
        null=False
    )
    
    class Meta:
        verbose_name = 'Boleta'
        verbose_name_plural = 'Boletas'

    def __str__(self):
        return 'Nº [' + str(self.id) + '] - ' + str(self.fecha_atencion)
            


class boletaServicio(models.Model):

    boleta = models.ForeignKey(
        Boleta, 
        on_delete=models.CASCADE,
        verbose_name='boleta'
    )
    