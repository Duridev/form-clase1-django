from django.shortcuts import render
from .forms import ContactoForm

def contacto_view(request):
    form = ContactoForm()
    return render(request, "formulario.html", {"form": form})

