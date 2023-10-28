from django.db import models

class Persona(models.Model):
    ID = models.IntegerField(primary_key=True, default=999)
    Nombre = models.CharField(max_length=255, default="Memingo")
    Edad = models.IntegerField(default=19)
    Ocupacion = models.CharField(max_length=255)

    class Meta:
        db_table = 'personas'

    def __str__(self):
        return self.Nombre

