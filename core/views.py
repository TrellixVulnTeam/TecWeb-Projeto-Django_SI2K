from django.shortcuts import render

def index(requisicao):

    contexto={
        "faculdade":"FACULDADES PAULISTAS UNIDAS",
        "facul":"FAPALUN",
        "pagina":"HomePage"
    }

    return render(requisicao,"index.html",contexto)


def cadastro(requisicao):
    return render(requisicao,"cadastro.html")



def contato(requisicao):
    return render(requisicao,"contato.html")



def cursos(requisicao):
    return render(requisicao,"cursos.html")



def login(requisicao):
    return render(requisicao,"login.html")



def noticias(requisicao):
    return render(requisicao,"noticias.html")



def novos_alunos(requisicao):
    return render(requisicao,"novos_alunos.html")