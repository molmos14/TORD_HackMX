from django.http import HttpResponse
from .models import Persona
from django.shortcuts import render
import FeelsAI.templates 
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import plotly.graph_objects as go
from FeelsAI.dashapps.example import app

def personas(request):
    todas = Persona.objects.all()
    data = ''
    for persona in todas:
        data += f'Nombre: {persona.Nombre}'
        data += "<br>"
    return HttpResponse(data)

def grafica(request):
    # Crea una lista de valores para el eje y
    y = list(range(1000))

    # Crea una gráfica usando Plotly
    fig = go.Figure(
        data=[go.Bar(y=y)]
    )

    # Convierte la gráfica en HTML
    grafica = fig.to_html(full_html=False)

    # Pasa la gráfica a la plantilla
    return render(request, 'graphic.html', {'grafica': grafica})

def dashboard(request):
    return render(request, 'dashboard.html')