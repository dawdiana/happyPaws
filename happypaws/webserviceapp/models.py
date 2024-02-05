# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


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
    nombreusuario = models.CharField(db_column='nombreUsuario', max_length=30)  # Field name made lowercase.
    contrasena = models.CharField(max_length=150)
    token = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tUsuarios'
