from django.db import models

# Create your models here.

class Residencia(models.Model):
    numero = models.PositiveIntegerField(unique=True)

    def __str__(self):
        return str(self.numero)


class Correspondencia(models.Model):

    TIPOS = [
        ('carta', 'CARTA'),
        ('encomienda', 'ENCOMIENDA'),
        ('delivery', 'DELIVERY'),
    ]

    ESTADOS = [
        ('Pendiente', 'Pendiente'),
        ('Entregada', 'Entregada'),
    ]

    residencia = models.ForeignKey(
        Residencia,
        on_delete=models.PROTECT
    )

    tipo = models.CharField(
        max_length=20,
        choices=TIPOS
    )

    descripcion = models.TextField(blank=True)

    fecha_recepcion = models.DateTimeField(
        auto_now_add=True
    )

    estado = models.CharField(
        max_length=10,
        choices=ESTADOS,
        default='Pendiente'
    )

    conserje = models.ForeignKey(
        'auth.User',
        on_delete=models.PROTECT
    )

    def __str__(self):
        return f'{self.tipo} - Residencia {self.residencia.numero}'
