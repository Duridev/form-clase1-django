from django.shortcuts import render
from .forms import ContactoForm


def index(request):
    if request.method == "POST":
        form = ContactoForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            return render(request, "formulario/exito.html")
    else:
        form = ContactoForm()
    return render(request, "formulario/index.html", {"form": form})

def exito(request):
    return render(request, "formulario/exito.html")