import os
import requests
from requests.auth import HTTPBasicAuth
from config import GITHUB_USERNAME, BITBUCKET_USERNAME, BITBUCKET_APP_PASSWORD, WORKSPACE, FILTER_KEYWORD

# URL base da API do Bitbucket
bitbucket_url = f'https://api.bitbucket.org/2.0/repositories/{WORKSPACE}'

# Autenticação do Bitbucket
bitbucket_auth = HTTPBasicAuth(BITBUCKET_USERNAME, BITBUCKET_APP_PASSWORD)

# Função para corrigir a URL de clonagem para usar SSH
def correct_bitbucket_url(url):
    # Usar o formato SSH para Bitbucket
    if url.startswith('https://'):
        repo_slug = url.split('/')[-1].replace('.git', '')
        return f'git@bitbucket.org:{WORKSPACE}/{repo_slug}.git'
    return url

# Função para criar repositório no GitHub e importar o conteúdo diretamente via SSH
def create_and_import_repo(repo_name, bitbucket_repo_url):
    # Corrigir a URL de clonagem para SSH
    bitbucket_repo_url = correct_bitbucket_url(bitbucket_repo_url)
    
    # Criar o repositório no GitHub
    create_command = f'gh repo create {GITHUB_USERNAME}/{repo_name} --private'
    create_result = os.system(create_command)
    
    if create_result == 0:
        print(f"Repositório {repo_name} criado no GitHub com sucesso.")
        
        # Clonar o repositório do Bitbucket e empurrar para o GitHub
        clone_command = f'git clone --mirror {bitbucket_repo_url} {repo_name}.git && cd {repo_name}.git && git push --mirror git@github.com:{GITHUB_USERNAME}/{repo_name}.git'
        clone_result = os.system(clone_command)
        
        if clone_result == 0:
            print(f"Repositório {repo_name} clonado com sucesso do Bitbucket para o GitHub.")
            return True
        else:
            print(f"Erro ao clonar o repositório {repo_name} do Bitbucket.")
            return False
    else:
        print(f"Erro ao criar o repositório {repo_name} no GitHub.")
        return False

# Loop para buscar todos os repositórios do Bitbucket e migrar para o GitHub
next_url = bitbucket_url

while next_url:
    response = requests.get(next_url, auth=bitbucket_auth)
    data = response.json()

    # Filtrar repositórios baseados no filtro configurado
    for repo in data['values']:
        project = repo.get('project', {})
        project_name = project.get('name', '').lower()
        project_slug = project.get('key', '').lower()

        # Filtra apenas repositórios de projetos que contenham a palavra-chave no nome ou slug
        if FILTER_KEYWORD.lower() in project_name or FILTER_KEYWORD.lower() in project_slug:
            repo_name = repo['slug']
            bitbucket_repo_url = repo['links']['clone'][1]['href']  # Usando o link SSH para clonar

            print(f"Migrando repositório {repo_name} do projeto {project_name}...")

            # Criar o repositório no GitHub e já clonar o conteúdo do Bitbucket
            create_and_import_repo(repo_name, bitbucket_repo_url)

    # Paginação: Se houver mais páginas, continuar a busca
    next_url = data.get('next', None)
