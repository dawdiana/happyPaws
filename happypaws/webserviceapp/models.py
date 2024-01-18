# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Tanimales(models.Model):
    nombre = models.CharField(max_length=25, blank=True, null=True)
    url_imagen = models.CharField(max_length=3000, blank=True, null=True)
    edad = models.CharField(max_length=20, blank=True, null=True)
    especie = models.CharField(max_length=20, blank=True, null=True)
    raza = models.CharField(max_length=20, blank=True, null=True)
    genero = models.CharField(max_length=15, blank=True, null=True)
    descripcion = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tAnimales'


class Tnoticias(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    tituloportada = models.CharField(db_column='tituloPortada', max_length=100, blank=True, null=True)  # Field name made lowercase.
    url_imagen = models.CharField(max_length=3000, blank=True, null=True)
    info_noticia = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tNoticias'


class Tproductos(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    url_imagen = models.CharField(max_length=3000, blank=True, null=True)
    precio = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    marca = models.CharField(max_length=25, blank=True, null=True)
    stock = models.IntegerField(blank=True, null=True)
    tipoproducto = models.CharField(db_column='tipoProducto', max_length=30, blank=True, null=True)  # Field name made lowercase.
    tipoanimal = models.CharField(db_column='tipoAnimal', max_length=30, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tProductos'


class Tusuarios(models.Model):
    nombre = models.CharField(max_length=20, blank=True, null=True)
    ap1 = models.CharField(max_length=25, blank=True, null=True)
    ap2 = models.CharField(max_length=25, blank=True, null=True)
    correo = models.CharField(max_length=50, blank=True, null=True)
    url_imagen = models.CharField(max_length=3000, blank=True, null=True)
    telefono = models.CharField(max_length=9, blank=True, null=True)
    dirreccion = models.CharField(max_length=35)
    nombreusuario = models.CharField(db_column='nombreUsuario', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cp = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tUsuarios'
