from django.db import models
#Modelo de Escritura (Commands)
class CourseCommand(models.Model): # Se define el modelo CourseCommand
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'courses'  # Se usa la misma tabla para lectura y escritura

# Modelo de Lectura (Queries)
class CourseQuery(models.Model): # Se define el modelo CourseQuery
    id = models.IntegerField(primary_key=True)  # Mantiene la clave primaria para que Django lo reconozca
    title = models.CharField(max_length=100)
    description = models.TextField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = 'courses'  # Usa la misma tabla
        managed = False  # Indica que Django no debe modificar la tabla