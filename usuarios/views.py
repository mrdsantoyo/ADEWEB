from django.shortcuts import render, redirect
from .forms import RegistroUsuarioForm

# Create your views here.

def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'registration/register.html', {'form': form})
