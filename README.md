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

Export estático (para GitHub Pages)

Este projeto é um aplicativo Django — ou seja, precisa de um servidor Python para funcionar completamente. O GitHub Pages só serve sites estáticos (HTML/CSS/JS) e não executa código Python.

Duas opções para publicar:

- 1) Converter para site estático e publicar no GitHub Pages (recomendado se você não precisa do backend dinâmico)

	- Use o script `export_static.py` para gerar uma versão estática do site em `docs/` (o GitHub Pages pode servir a pasta `docs/`):

		```bash
		# Ative o virtualenv e instale dependências antes
		python export_static.py
		git add docs/ && git commit -m "Add static export" && git push
		```

	- Vá nas configurações do repositório -> Pages e selecione a pasta `docs/` como fonte.

	- Limitações: formulários, uploads, pesquisa e outras funcionalidades que dependem de backend não funcionarão. Links gerados com prefix absoluto podem precisar de ajuste se você publicar em um subpath.

- 2) Deploy em um host que rode Django (recomendado para funcionalidade completa)

	- Plataformas recomendadas: Render, Railway, Fly, PythonAnywhere, DigitalOcean App Platform ou um servidor/VM próprio.
	- Alternativamente, use Docker (veja abaixo) e publique numa VM.

Docker (opcional)

Você pode construir um `Dockerfile` e `docker-compose.yml` para facilitar o deploy. Se quiser, eu posso adicionar um `Dockerfile` e um `docker-compose.yml` prontos.

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