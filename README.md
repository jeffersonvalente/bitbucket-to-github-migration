# Bitbucket to GitHub Migration 🚀

Simplifique a migração de repositórios do **Bitbucket** para o **GitHub** de forma automatizada, segura e eficiente. Este script foi criado para resolver desafios comuns enfrentados por equipes técnicas, economizando tempo e garantindo a consistência na integração de repositórios.

Seja para reorganizar projetos ou integrar novos times, esta ferramenta facilita o processo, reduz erros e elimina tarefas repetitivas.

---

## 🛠 Funcionalidades

- **Migração Totalmente Automatizada:** Reduza o esforço manual ao transferir repositórios do Bitbucket para o GitHub.
- **Filtro Configurável:** Personalize o filtro de migração para atender às necessidades específicas do seu projeto (ex.: filtrar por palavras-chave no nome ou slug).
- **URLs SSH:** Garante segurança e confiabilidade durante a transferência dos repositórios.
- **Paginação de Resultados:** Gerencia automaticamente workspaces grandes no Bitbucket.
- **Criação de Repositórios no GitHub:** Cria repositórios privados de forma automática, garantindo organização e segurança.

---

## 📋 Requisitos

1. **Python 3.x** instalado.
2. **GitHub CLI (`gh`)** configurado. [Guia de instalação](https://cli.github.com/manual/installation)
3. **Git** instalado na máquina.
4. **App Password do Bitbucket** configurado com permissões de leitura. [Guia de geração](https://bitbucket.org/account/settings/app-passwords/)
5. Instale as dependências do Python:
   ```bash
   pip install requests
   ```

---

## ⚙️ Configuração

1. No arquivo `config.py`, já incluído no repositório, edite as variáveis de configuração:

   ```python
   GITHUB_USERNAME = 'seu_usuario_github'
   BITBUCKET_USERNAME = 'seu_usuario_bitbucket'
   BITBUCKET_APP_PASSWORD = 'seu_app_password_bitbucket'
   WORKSPACE = 'seu_workspace'
   FILTER_KEYWORD = 'sua_palavra_chave'  # Exemplo: 'Devops, prd, app_XXX'
   ```

2. Salve o arquivo `config.py` com suas configurações.

3. Execute o script para iniciar a migração:

   ```bash
   python migrar_repos.py
   ```

---

## 🧩 Como Funciona?

1. **Busca Repositórios:** O script acessa a API do Bitbucket para listar os repositórios do workspace configurado.
2. **Aplica o Filtro:** Seleciona apenas os repositórios que correspondem à palavra-chave configurada.
3. **Criação no GitHub:** Cria automaticamente os repositórios no GitHub como privados.
4. **Transferência via SSH:** Clona os repositórios do Bitbucket e realiza o push para o GitHub, garantindo uma transferência segura e rápida.

---

## 🌟 Exemplos Práticos

### Cenário 1: Integração de Times em Nova Organização

Facilita a transição para uma nova organização ao migrar repositórios de maneira automatizada, garantindo consistência nos pipelines.

### Cenário 2: Reorganização de Projetos

Centralize repositórios dispersos entre Bitbucket e GitHub em um único local, simplificando o monitoramento e a integração.

---

## 📈 Benefícios Técnicos

- **Automação Inteligente:** Evita tarefas manuais repetitivas, reduzindo o risco de erros humanos.
- **Segurança Integrada:** URLs SSH garantem que a transferência seja segura e confiável.
- **Escalabilidade:** Projetado para workspaces grandes, com suporte à paginação de repositórios.
- **Flexibilidade:** Adapte o filtro para atender diferentes necessidades organizacionais.

---

## 🤝 Contribuindo

Este projeto foi desenvolvido para ser extensível. Sugestões e melhorias são sempre bem-vindas! Faça um fork e envie seu pull request.

---

## 📢 Contato

Se você tiver dúvidas, entre em contato:

- [LinkedIn](https://www.linkedin.com/in/jefferson-hoy-valente/)  

