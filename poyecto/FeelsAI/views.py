from django.http import HttpResponse
from .models import prediccion
from django.shortcuts import render
import FeelsAI.templates 
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import plotly.graph_objects as go
from FeelsAI.dashapps.example import app
import numpy as np
from .models import prediccion
import plotly.express as px
import pandas as pd

def home(request):
    return render(request, 'home.html')

def see_prediction(request):
    todas = prediccion.objects.all()

    # Crear un diccionario para almacenar los datos
    data_dict = {}

    for persona in todas:
        username = persona.username
        lvlA_value = str(persona.lvlA)  # Convertir a cadena

        if username in data_dict:
            data_dict[username].append(lvlA_value)
        else:
            data_dict[username] = [lvlA_value]

    # Crear un arreglo de NumPy para almacenar los datos
    data_array = []

    for username, values in data_dict.items():
        data_array.append([username] + values)

    # Asegurarse de que todas las filas tengan la misma longitud
    max_length = max(len(row) for row in data_array)
    for row in data_array:
        while len(row) < max_length:
            row.append('')  # Agregar elementos vacíos si es necesario

    # Convertir la lista en un arreglo NumPy
    data_np_array = np.vstack(data_array)

    # Convertir el arreglo de NumPy a una cadena para imprimir
    data_str = np.array2string(data_np_array, separator='  ')

    return HttpResponse(data_str)

def grafica(request):

    df=pd.read_csv("/Users/elang/OneDrive/Escritorio/HackMX/TORD_HACKMX/poyecto/Final/StressLevelDataset.csv")
    df1=df.drop(columns=['self_esteem','sleep_quality','living_conditions','safety','basic_needs','academic_performance','teacher_student_relationship','social_support','blood_pressure','breathing_problem'])
    fig = px.sunburst(df1, path=['depression', 'mental_health_history'],
        values='anxiety_level')
    #fig.show()

    # # Crea una lista de valores para el eje y
    # y = list(range(1000))

    # # Crea una gráfica usando Plotly
    # fig = go.Figure(
    #     data=[go.Bar(y=y)]
    # )

    # # Convierte la gráfica en HTML
    grafica = fig.to_html(full_html=False)

    # # Pasa la gráfica a la plantilla
    return render(request, 'graphic.html', {'grafica': grafica})