from django.db import models

class prediccion(models.Model):
    date = models.DateField(default='2023/10/18')
    lvlA = models.FloatField(max_length=100, default=0.5)
    username = models.CharField(max_length=100,primary_key=True, default='memin')

    class Meta:
        db_table = 'prediccion'

    def __str__(self):
        return self.username

