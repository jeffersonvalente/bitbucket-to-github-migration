
# Bitbucket to GitHub Migration — Automação de Migração de Repositórios

Esse projeto automatiza a migração de repositórios do Bitbucket para o GitHub, com foco em segurança, rastreabilidade e escalabilidade.  
Resolve dores comuns enfrentadas por equipes que precisam reorganizar projetos ou integrar times em novos ambientes, sem perder tempo com tarefas repetitivas.

---

## O que esse script faz

- Busca todos os repositórios do Bitbucket (com paginação)
- Aplica filtro por palavra-chave no nome ou slug
- Cria repositórios privados no GitHub
- Clona via SSH e faz push de cada repositório
- Usa configuração parametrizada via `config.py`

---

## Pré-requisitos

- Python 3.x
- Git instalado
- GitHub CLI (`gh`) configurado: https://cli.github.com/manual/installation
- App Password do Bitbucket com permissão de leitura: https://bitbucket.org/account/settings/app-passwords/

Instale a dependência:

```bash
pip install requests
```

---

## Como configurar

1. Edite o arquivo `config.py`:

```python
GITHUB_USERNAME = 'seu_usuario_github'
BITBUCKET_USERNAME = 'seu_usuario_bitbucket'
BITBUCKET_APP_PASSWORD = 'seu_app_password_bitbucket'
WORKSPACE = 'seu_workspace'
FILTER_KEYWORD = 'sua_palavra_chave'
```

2. Rode o script:

```bash
python migrar_repos.py
```

---

## Como funciona

```plaintext
1. Acessa a API do Bitbucket e lista os repositórios
2. Aplica o filtro configurado
3. Cria repositórios no GitHub com nome equivalente
4. Clona do Bitbucket e envia pro GitHub via SSH
```

---

## Casos de uso

- Integração de times em nova organização GitHub
- Reorganização de projetos dispersos entre plataformas
- Padronização de estrutura de repositórios

---

## Por que usar?

Automatizar essa migração poupa tempo, reduz erro humano e mantém rastreabilidade.  
Serve tanto pra times pequenos reorganizando ambientes, quanto pra estruturas maiores com centenas de repositórios.

---

## Contribuições

Sugestões são bem-vindas.  
Esse projeto foi feito pra ser adaptável — se quiser melhorar algo, mande um pull request.

---

## Contato

LinkedIn: https://www.linkedin.com/in/jefferson-hoy-valente/
