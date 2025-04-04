from django.db import models
from django.contrib.auth import get_user_model
from datetime import date
from dateutil.relativedelta import relativedelta
from django.core.exceptions import ValidationError

User = get_user_model()

ESTATUS_DOCUMENTO = [
    ('ACTIVO','Activo'),
    ('OBSOLETO','Obsoleto'),
    ('ELABORACION','En Elaboración'),
    ('ACTUALIZACION', 'En Actualización'),
    ('REVISION','En Revisión'),
    ('APROBACION','En Aprobación'),
    ('PUBLICADO','Publicado'),
]

TIPO_DOCUMENTO = [
    ('PROCEDIMIENTO', 'Procedimiento'),
    ('MANUAL', 'Manual'),
    ('INSTRUCTIVO','Instructivo'),
    ('FORMATO','Formato'),
]

FRECUENCIA_EVALUACION = [
    (1, '1 mes'), 
    (2, '2 meses'), 
    (3, '3 meses'),
    (4, '4 meses'), 
    (5, '5 meses'), 
    (6, '6 meses'), 
    (12, '12 meses'),
]

def validar_codigo(value):
    if not value.startswith('DOC-'):
        raise ValidationError('El código debe comenzar con "DOC-"')

def ruta_documentos(instance, filename):
    return f'adeweb/documentaciondocumentos/{instance.codigo}/{filename}'

class Normas(models.Model):
    norma = models.CharField(max_length=50)
    punto_norma = models.CharField(max_length=50)

class Documentos(models.Model):
    tipo_de_documento = models.CharField(choices=TIPO_DOCUMENTO, max_length=50)
    codigo = models.CharField(max_length=50, validators=[validar_codigo])
    nombre_documento = models.CharField(max_length=100)
    estatus = models.CharField(choices=ESTATUS_DOCUMENTO, max_length=20)
    version = models.IntegerField()
    frecuencia_evaluacion = models.IntegerField(choices=FRECUENCIA_EVALUACION)
    vigencia_documento = models.DateField()
    localidad = models.CharField(max_length=50)
    creador = models.CharField(max_length=50)

    carpeta = models.CharField(max_length=100)
    documento_original = models.FileField(upload_to=ruta_documentos, max_length=100)

    norma = models.ForeignKey(Normas, on_delete=models.DO_NOTHING, related_name='documentos_norma')
    punto_norma = models.ForeignKey(Normas, on_delete=models.DO_NOTHING, related_name='documentos_punto_norma')

    usuarios_distribucion = models.JSONField(blank=True, default=list)
    grupos_distribucion = models.JSONField(blank=True, default=list)
    puestos_distribucion = models.JSONField(blank=True, default=list)
    procesos_distribucion = models.JSONField(blank=True, default=list)
    documentos_relacionados = models.JSONField(blank=True, default=list)

    revisor = models.JSONField(blank=True, default=list)
    aprobador = models.JSONField(blank=True, default=list)
    publicador = models.JSONField(blank=True, default=list)
    
    fecha_publicacion = models.DateField(auto_now_add=True)
    fecha_actualizacion = models.DateField(null=True, auto_now=True)
    fecha_obsoleto = models.DateField(null=True, blank=True)

    comentarios_alta = models.TextField(blank=True)
    motivo_cambio = models.TextField(blank=True)
    motivo_baja = models.TextField(blank=True)

    def alta_documento(self):
        if not self.pk:
            self.estatus = 'ELABORACION'
            self.vigencia_documento = date.today() + relativedelta(months=self.frecuencia_evaluacion)
            self.carpeta = f"adeweb/documentaciondocumentos/{self.codigo}/"
            self.save()
        else:
            raise Exception("El documento ya fue dado de alta.")

    def baja_documento(self):
        if self.pk:
            self.estatus = 'OBSOLETO'
            self.fecha_obsoleto = date.today()
            self.save()
        else:
            raise Exception("El documento no existe.")

    def solicitud_cambio(self, nueva_version):
        if self.estatus != 'OBSOLETO':
            self.estatus = 'ACTUALIZACION'
            self.version = nueva_version if self.version < 1 else self.version + 1
            self.save()
        else:
            raise Exception("No se puede solicitar cambio de un documento obsoleto.")

    @classmethod
    def buscar_documentos(cls, **kwargs):
        return cls.objects.filter(**kwargs)

    def registrar_evento(self, usuario, accion):
        RegistroEvento.objects.create(
            documento=self,
            usuario=usuario,
            accion=accion,
        )

    def __str__(self):
        return f"Documento {self.codigo} (v{self.version}) en estatus ({self.estatus}) publicado el {self.fecha_publicacion}"


class RegistroEvento(models.Model):
    documento = models.ForeignKey(Documentos, on_delete=models.DO_NOTHING, related_name='eventos')
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    accion = models.CharField(max_length=100)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.fecha.strftime('%Y-%m-%d %H:%M')}] {self.usuario} realizó: {self.accion} en {self.documento.codigo}"
