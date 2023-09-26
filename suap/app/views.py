from django.shortcuts import render
from . models import*
# Create your views here.

def area(request):
    consultas = {
        'consultas':Area.objects.all()
    }
    return render(request, 'consulta/Area.html',consultas)

def avaliacao(request):
    consultas = {
        'consultas':Avaliacao.objects.all()
    }
    return render(request, 'consulta/Avaliacao.html',consultas)

def cidade(request):
    consultas = {
        'consultas':Cidade.objects.all()
    }
    return render(request, 'consulta/Cidade.html',consultas)

def curso(request):
    consultas = {
        'consultas':Curso.objects.all()
    }
    return render(request, 'consulta/Curso.html',consultas)

def disciplina(request):
    consultas = {
        'consultas':Disciplina.objects.all()
    }
    return render(request, 'consulta/Disciplina.html',consultas)

def disciplinacursos(request):
    consultas = {
        'consultas':DisciplinaCursos.objects.all()
    }
    return render(request, 'consulta/DisciplinaCursos.html',consultas)

def frequencia(request):
    consultas = {
        'consultas':Frequencia.objects.all()
    }
    return render(request, 'consulta/Frequencia.html',consultas)

def instituicao(request):
    consultas = {
        'consultas':Instituicao.objects.all()
    }
    return render(request, 'consulta/Instituicao.html',consultas)

def matricula(request):
    consultas = {
        'consultas':Matricula.objects.all()
    }
    return render(request, 'consulta/Matricula.html',consultas)

def ocorrencia(request):
    consultas = {
        'consultas':Ocorrencia.objects.all()
    }
    return render(request, 'consulta/Ocorrencia.html',consultas)

def ocupacao(request):
    consultas = {
        'consultas':Ocupacao.objects.all()
    }
    return render(request, 'consulta/Ocupacao.html',consultas)

def periodo(request):
    consultas = {
        'consultas':Periodo.objects.all()
    }
    return render(request, 'consulta/Periodo.html',consultas)

def pessoa(request):
    consultas = {
        'consultas':Pessoa.objects.all()
    }
    return render(request, 'consulta/Pessoa.html',consultas)

def tipoavaliacao(request):
    consultas = {
        'consultas':TipoAvaliacao.objects.all()
    }
    return render(request, 'consulta/TipoAvaliacao.html',consultas)

def turma(request):
    consultas = {
        'consultas':Turma.objects.all()
    }
    return render(request, 'consulta/Turma.html',consultas)
