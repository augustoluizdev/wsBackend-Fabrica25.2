from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Pessoa, Livro, LivroFavorito
from .forms import PessoaForm, LivroForm
import requests



def get_pessoa(request):
    pessoa_id = request.session.get('pessoa_id')
    if pessoa_id:
        return Pessoa.objects.filter(id=pessoa_id).first()
    return None


def criar_pessoa(request):
    pessoas = Pessoa.objects.all()
    form = PessoaForm()

    if request.method == "POST":
        form = PessoaForm(request.POST)
        if form.is_valid():
            pessoa = form.save()
            request.session['pessoa_id'] = pessoa.id
            return redirect('listar_livros_favoritos')
    return render(request, 'pessoas/criar_pessoa.html', {'form': form, 'pessoas': pessoas, 'pessoa_ativa': get_pessoa(request)})    

def salvar_pessoa(request, pessoa_id):
    request.session['pessoa_id'] = pessoa_id
    return redirect('criar_pessoa')

def atualizar_pessoa(request, pessoa_id):
    pessoa = get_object_or_404(Pessoa, id=pessoa_id)
    if request.method == "POST":
        form = PessoaForm(request.POST, instance=pessoa)
        if form.is_valid():
            form.save()
            return redirect('criar_pessoa')
    else:
        form = PessoaForm(instance=pessoa)
    return render(request, 'pessoas/atualizar_pessoa.html', {'form': form, 'pessoa': pessoa})  

def deletar_pessoa(request, pessoa_id):
    pessoa = get_object_or_404(Pessoa, id=pessoa_id)
    if request.method == "POST":
        pessoa.delete()
        return redirect('criar_pessoa')
    return render(request, 'pessoas/confirmar_delete.html', {'pessoa':pessoa})


def buscar_livro(isbn):
    url = f"https://openlibrary.org/isbn/{isbn}.json"
    response = requests.get(url)
    if response.status_code == 200:
        dados = response.json()
        titulo = dados.get('title', 'Sem título')
        autores = dados.get('authors', [])
        autor_nome = "Desconhecido"
        if autores:
            autor_data = requests.get(f"https://openlibrary.org{autores[0]['key']}.json")
            if autor_data.status_code == 200:
                autor_nome = autor_data.json().get('name', "Desconhecido")
        return {'titulo': titulo, 'autor': autor_nome, 'isbn': isbn}
    return None

def adicionar_livro(request):
    form = LivroForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        isbn = form.cleaned_data['isbn']
        dados = buscar_livro(isbn)
        if dados:
            livro, _ = Livro.objects.get_or_create(
                isbn=isbn,
                defaults={'titulo': dados['titulo'], 'autor': dados['autor']}
            )
            return redirect('checar_livro', livro.id)
        else:
            messages.error(request, "Livro não encontrado!")
    return render(request, 'livros/adicionar_livro.html', {'form': form})

def checar_livro(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id)
    pessoa = get_pessoa(request) 
    if not pessoa:
        return redirect('criar_pessoa')

    ja_favorito = LivroFavorito.objects.filter(pessoa=pessoa, livro=livro).exists()
    return render(request, 'livros/checar_livro.html', {'livro': livro, 'ja_favorito': ja_favorito})

def favoritar_livro(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id)
    pessoa = get_pessoa(request)
    if not pessoa:
        return redirect('criar_pessoa')

    LivroFavorito.objects.get_or_create(pessoa=pessoa, livro=livro)
    return redirect('checar_livro', livro_id)

def listar_favoritos(request):
    pessoa = get_pessoa(request)
    if not pessoa:
        return redirect('criar_pessoa')
    
    favoritos = LivroFavorito.objects.filter(pessoa=pessoa).select_related('livro')
    return render(request, 'livros/favoritos.html', {'favoritos': favoritos, 'pessoa': pessoa})
