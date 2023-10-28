"""poyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from FeelsAI.views import see_prediction
from FeelsAI.views import grafica
from FeelsAI.views import dashboard
from FeelsAI.dashapps.example import app
from django.urls import include
from FeelsAI.views import home 


urlpatterns = [
    path('', home, name='home'),
    path('sql/', see_prediction, name='sql'),
    path('grafica/', grafica, name='grafica'),
    path('dashboard/', dashboard, name='dashboard'),
    path('django_plotly_dash/', include('django_plotly_dash.urls')),
    # Otras rutas de tu aplicación
]