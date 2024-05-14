from django.shortcuts import render
from .models import Usuario

# Create your views here.
def home(request):
    return render(request, 'usuarios/home.html')

def usuarios(request):
    # Salvar os dados da tela p/ o bd
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()

    # Exibir todos os usuários do bd em uma nova página
    usuarios = {
        'usuarios': Usuario.objects.all()
    }

    # Retornar dados para a página de listagem de usuários
    return render(request, 'usuarios/usuarios.html', usuarios)