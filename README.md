# MOCS - Django scaffold

Este repositório contém um esqueleto de projeto Django para o site do MOCS (Modelo de Comitês Simulados) com um app `mocs_app` e templates prontos.

Como rodar localmente (Ubuntu / Bash):

1. Criar e ativar um ambiente virtual

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Instalar dependências

```bash
pip install -r requirements.txt
```

3. Aplicar migrações e criar superusuario

```bash
python manage.py migrate
python manage.py createsuperuser
```

4. Rodar servidor de desenvolvimento

```bash
python manage.py runserver
```

Arquivos-chave:

- `manage.py` — utilitário do Django
- `mocs_project/` — configuração do projeto (settings, urls, wsgi)
- `mocs_app/` — app principal com models, views, admin e urls
- `templates/` — templates base e páginas
- `requirements.txt` — dependências

Observações:

- A chave `SECRET_KEY` em `mocs_project/settings.py` é um placeholder; substitua-a antes de publicar em produção.
- Em desenvolvimento, uploads são servidos via `MEDIA_URL` quando `DEBUG=True`.
- Tailwind é carregado via CDN no `base.html` para facilitar o setup inicial.
# Mocs