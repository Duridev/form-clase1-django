from django.shortcuts import render
from .forms import ContactoForm

def index(request):
    form = ContactoForm()
    return render(request, 'formulario/index.html', {'form' : form})

# def contacto_view(request):
#     if request.method == "POST":
#         form = ContactoForm(request.POST)
#         if form.is_valid():
#             nombre = form.cleaned_data["nombre"]
#     else:
#         form = ContactoForm()
        
#     return render(request, "formulario.html", {"form": form})

