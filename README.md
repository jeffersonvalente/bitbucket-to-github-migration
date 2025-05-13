# Automação de Migração de Repositórios do Bitbucket para o GitHub

Este case documenta a criação de um script em Python para automatizar a migração de repositórios do Bitbucket para o GitHub — com preservação completa de histórico de commits, branches e nomenclatura original.

A solução nasceu de um cenário crítico de transição de plataforma, onde migrar manualmente mais de 270 repositórios era inviável técnica e operacionalmente — tanto pelo volume, quanto pelo prazo e risco de perda de rastreabilidade.

## Objetivo

Evitar perda de histórico, inconsistência entre ambientes e erros humanos durante uma migração em larga escala, garantindo:

- Preservação de branches, commits e nomes originais
- Capacidade de filtrar e priorizar o que seria migrado
- Migração segura via SSH e repositórios privados
- Execução confiável, rastreável e documentada

## Desafios técnicos

Durante o desenvolvimento, enfrentei desafios importantes:

- A API do Bitbucket exigia paginação para lidar com grandes volumes
- O Bitbucket possui o conceito de "projetos", inexistente no GitHub — o que exigiu adaptação lógica para recriar estrutura organizacional sem perdas
- Controle de acesso via App Password e SSH para garantir segurança na transferência
- Existência de repositórios com naming inconsistente ou que não deveriam ser migrados — resolvido com filtros por prefixo/sufixo configuráveis

## Decisões técnicas

- A linguagem escolhida foi **Python**, pela clareza, adaptabilidade e familiaridade com a stack do time
- A **CLI oficial do GitHub (gh)** foi usada para automatizar a criação de repositórios privados, respeitando permissões
- A estrutura do script foi pensada para permitir manutenção futura por outros devs, com configuração simples via `config.py`

## Resultado entregue

- Script funcional, validado e aplicado em ambiente real
- Capaz de clonar qualquer repositório Bitbucket, preservar histórico e publicar automaticamente no GitHub
- Comportamento controlado por filtros — permitindo selecionar só os repositórios desejados
- Migração segura, 100% rastreável e replicável

O feedback do time foi imediato: a automação reduziu drasticamente o tempo de execução, eliminou erros manuais e trouxe previsibilidade ao processo de transição.

## Aprendizados

A manipulação de estruturas como “projetos” e nomes inconsistentes exigiu decisões práticas e tratamento lógico refinado.  
A entrega demonstrou o impacto direto de uma automação sob medida em cenários de urgência, escala e criticidade operacional.

Se eu fosse refazer hoje, com base no que aprendi durante e após a entrega:

- Otimizaria a execução com paralelismo controlado para acelerar a migração em ambientes com centenas de repositórios
- Adicionaria geração de logs persistentes para rastreabilidade pós-migração
- Criaria testes unitários básicos para as funções de autenticação, filtro e paginação
- Melhoraria a UX do terminal com feedback visual mais estruturado, como progresso e sumário ao final
- Validaria pré-requisitos como existência do gh CLI e conectividade com as APIs antes da execução

## Como usar

1. Renomeie o arquivo `config_example.py` para `config.py`
2. Preencha com suas credenciais reais:
   - GitHub username
   - Bitbucket username e app password
   - Workspace e palavra-chave de filtro

3. Certifique-se de que o GitHub CLI (`gh`) esteja instalado e autenticado:
   ```bash
   gh auth login
   ```

4. Execute o script principal:
   ```bash
   python3 migrate.py
   ```

> O script irá buscar todos os repositórios do Bitbucket com base no filtro configurado, criar os equivalentes no GitHub e clonar via SSH com preservação completa de histórico.

## Contato

[LinkedIn — Jefferson Hoy Valente](https://www.linkedin.com/in/jefferson-hoy-valente/)
