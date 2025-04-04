from django import forms
from .models import Documentos
# from django.contrib.auth.models import User


class AltaDocumentoForm(forms.ModelForm):
    class Meta:
        model = Documentos
        exclude = [
            'estatus',
            'creador',
            'vigencia_documento',
            'fecha_actualizacion',
            'fecha_publicacion',
            'fecha_obsoleto',
            ]
        widgets = {
            'comentarios_alta': forms.Textarea(attrs={'rows': 3}),
            'motivo_cambio': forms.Textarea(attrs={'rows': 3}),
            'motivo_baja': forms.Textarea(attrs={'rows': 3}),
            'frecuencia_evaluacion': forms.Select(),
            'tipo_de_documento': forms.Select(),
            }
        
        