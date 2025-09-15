# wsBackend-Fabrica25.2

Backend em Django para gerenciamento de livros e favoritos, com cadastro de pessoas.

---

## Tecnologias

- Python 3.x
- Django 4.x
- SQLite (padrão) / qualquer outro banco suportado pelo Django
- HTML, CSS, Templates Django

---

## Funcionalidades

- Adicionar e buscar livros.
- Listar livros favoritos de cada usuário.
- Remover livros favoritos com confirmação.
- Cadastro e gerenciamento de pessoas.

---

## Instalação

1. Clone o repositório:

```bash
git clone https://github.com/augustoluizdev/wsBackend-Fabrica25.2.git
```
2. Acesse a pasta do projeto:

```bash
cd wsBackend-Fabrica25.2
```
3. Crie um ambiente virtual:

```bash
python -m venv venv
```
4. Ative o ambiente virtual:
<br>
Windows:

```bash
venv\Scripts\activate
```
Linux / macOS:

```bash
source venv/bin/activate
```
5. Instale as dependências:

```bash
pip install -r requirements.txt
```
6. Faça as migrações do banco de dados:

```bash
python manage.py migrate
```
7. Execute o servidor:

```bash
python manage.py runserver
```


## Uso

- Acesse a página principal para adicionar e buscar livros.  
- Adicione livros aos favoritos clicando no botão correspondente.  
- Para remover um livro favorito, clique no botão **Remover**, confirme na página de confirmação.  
- Cadastre uma nova pessoa acessando a página de **Cadastro de Pessoa**, preenchendo os campos obrigatórios e salvando as informações.  
- Edite ou visualize os dados de uma pessoa já cadastrada para atualizar informações pessoais.
<hr>
<h2>Desenvolvedor: Augusto Luiz Lima Dantas<br>
GitHub: https://github.com/augustoluizdev</h2>
