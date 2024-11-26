from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class NodeData(models.Model):
    id = models.AutoField(primary_key=True) 
    node = models.CharField(
        max_length=100
    )  
    longitude = models.DecimalField(
        max_digits=9,  # Total de dígitos (incluyendo decimales)
        decimal_places=6,  # Número de decimales
        validators=[MinValueValidator(-180.0), MaxValueValidator(180.0)],
        help_text="Valor en grados, entre -180.0 y 180.0."
    )
    latitude = models.DecimalField(
        max_digits=9,  # Total de dígitos
        decimal_places=6,  # Número de decimales
        validators=[MinValueValidator(-90.0), MaxValueValidator(90.0)],
        help_text="Valor en grados, entre -90.0 y 90.0."
    )
    temperature = models.DecimalField(
        max_digits=5,  # Total de dígitos (por ejemplo, -50.00 es un valor válido)
        decimal_places=2,  # Número de decimales
        validators=[MinValueValidator(-50), MaxValueValidator(100)],
        help_text="Temperatura en grados Celsius, entre -50 y 100."
    )
    humidity = models.DecimalField(
        max_digits=5,  # Total de dígitos (por ejemplo, 100.0 es válido)
        decimal_places=2,  # Número de decimales
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text="Porcentaje de humedad, entre 0 y 100."
    )
    pressure = models.DecimalField(
        max_digits=7,  # Total de dígitos (por ejemplo, 1100.0 es válido)
        decimal_places=2,  # Número de decimales
        validators=[MinValueValidator(300), MaxValueValidator(1100)],
        help_text="Presión en hPa, entre 300 y 1100."
    )
    altitude = models.DecimalField(
        max_digits=7,  # Total de dígitos (por ejemplo, 9000.0 es válido)
        decimal_places=2,  # Número de decimales
        validators=[MinValueValidator(-500), MaxValueValidator(9000)],
        help_text="Altitud en metros, entre -500 y 9000."
    )
    timestamp = models.BigIntegerField(
        validators=[MinValueValidator(0)],
        help_text="Tiempo en formato UNIX (número entero positivo)."
    )

    def __str__(self):
        return f"Node: {self.node}, Timestamp: {self.timestamp}"
