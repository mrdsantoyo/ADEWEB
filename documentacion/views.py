from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import AltaDocumentoForm
from .models import Documentos


# Create your views here.

@login_required
def crear_documento(request):
    if request.method == 'POST':
        form = AltaDocumentoForm(request.POST, request.FILES)
        if form.is_valid():
            documento = form.save(commit=False)
            documento.creador = request.user.username

            try:
                documento.alta_documento()  # Esto hace .save()
                documento.registrar_evento(
                    usuario=request.user,
                    accion='Alta'
                )
                return redirect('documento_exito')  # Asegúrate que esta URL esté en tus urls.py
            except Exception as e:
                form.add_error(None, f"Ocurrió un error: {e}")
    else:
        form = AltaDocumentoForm()

    return render(request, 'documentos/crear_documento.html', {'form': form})


@login_required
def documento_exito(request):
    return HttpResponse("¡Documento creado con éxito!")
