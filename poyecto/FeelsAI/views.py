from django.http import HttpResponse
from .models import Persona

def personas(request):
    todas = Persona.objects.all()
    data = ''
    for persona in todas:
        data += f'Nombre: {persona.Nombre}'
        data += "<br>"
    return HttpResponse(data)
