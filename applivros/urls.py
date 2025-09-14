from django.urls import path
from . import views
from .views import criar_pessoa, salvar_pessoa, atualizar_pessoa, deletar_pessoa, adicionar_livro, checar_livro, favoritar_livro, listar_favoritos 


urlpatterns = [
    path('pessoas/', views.criar_pessoa, name='criar_pessoa'),
    path('pessoas/salvar/<int:pessoa_id>', views.salvar_pessoa, name='salvar_pessoa'),
    path('pessoas/atualizar/<int:pessoa_id>/', views.atualizar_pessoa, name='atualizar_pessoa'),
    path('pessoas/deletar/<int:pessoa_id>/', views.deletar_pessoa, name='deletar_pessoa'),

    path('adicionar/', views.adicionar_livro, name='adicionar_livro'),
    path('checar/<int:livro_id>/', views.checar_livro, name='checar_livro'), 
    path('checar/<int:livro_id>/favoritos/', views.favoritar_livro, name='favoritar_livro'),
    path('favoritos/', views.listar_favoritos, name='listar_livros_favoritos'),   
]
