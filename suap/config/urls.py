"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'),name='index'),
    path('Area/', area, name='area'),
    path('Avaliacao/', avaliacao, name='avaliacao'),
    path('Cidade/', cidade, name='cidade'),
    path('Curso/', curso, name='curso'),
    path('Disciplina/', disciplina, name='disciplina'),
    path('DisciplinaCursos/', disciplinacursos, name='disciplinacursos'),
    path('Frequencia/', frequencia, name='frequencia'),
    path('Instituicao/', instituicao, name='instituicao'),
    path('Matricula/', matricula, name='matricula'),
    path('Ocorrencia/', ocorrencia, name='ocorrencia'),
    path('Ocupacao/', ocupacao, name='ocorrencia'),
    path('Periodo/', periodo, name='periodo'),
    path('Pessoa/', pessoa, name='pessoa'),
    path('TipoAvaliacao/', tipoavaliacao, name='tipoavaliacao'),
    path('Turma/', turma, name='turma'),
]
