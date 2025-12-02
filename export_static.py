#!/usr/bin/env python3
"""
Exporta versões estáticas do site Django para a pasta `docs/` (útil para GitHub Pages).

Como funciona:
- Faz bootstrap do Django usando `mocs_project.settings`.
- Usa `django.test.Client` para requisitar as rotas desejadas por idioma.
- Salva o HTML em `docs/{lang}/.../index.html` (estrutura em diretórios).

Limitações:
- Funcionalidades dinâmicas (formulários, uploads, busca em tempo real) não funcionarão como backend.
- Links absolutos podem precisar de ajuste se for publicar em um subpath (ex: `https://user.github.io/repo/`).
"""
import os
import sys
from pathlib import Path


def ensure_django():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mocs_project.settings')
    try:
        import django
        django.setup()
    except Exception as e:
        print('Erro ao inicializar Django:', e)
        sys.exit(1)


def write_file(path: Path, content: bytes):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(content)


def main():
    ensure_django()

    from django.test import Client
    from django.urls import reverse
    from mocs_app.models import Post

    client = Client()

    docs_root = Path('docs')
    # Limpa pasta docs parcialmente (não remove se você tiver outros arquivos) - aqui removemos tudo para evitar restos
    if docs_root.exists():
        for p in docs_root.rglob('*'):
            try:
                if p.is_file():
                    p.unlink()
            except Exception:
                pass

    languages = ['pt', 'en', 'es']
    pages = ['', 'about', 'timeline', 'team', 'partners', 'shop', 'gallery', 'blog', 'events', 'contact', 'join']

    print('Gerando páginas estáticas em', docs_root)

    for lang in languages:
        for page in pages:
            # monta a URL: /pt/ or /pt/about/
            if page == '':
                url = f'/{lang}/'
                out_path = docs_root / lang / 'index.html'
            else:
                url = f'/{lang}/{page}/'
                out_path = docs_root / lang / page / 'index.html'

            print('GET', url)
            resp = client.get(url)
            if resp.status_code == 200:
                write_file(out_path, resp.content)
            else:
                print(f'  Aviso: {url} retornou status {resp.status_code} — escrevendo página de erro simples.')
                write_file(out_path, resp.content or b'')

    # Gerar páginas de detalhes de blog (se houver)
    for post in Post.objects.all():
        # A rota definida em urls.py é 'blog/<int:pk>/' dentro de i18n_patterns
        for lang in languages:
            url = f'/{lang}/blog/{post.pk}/'
            out_path = docs_root / lang / 'blog' / str(post.pk) / 'index.html'
            print('GET', url)
            resp = client.get(url)
            if resp.status_code == 200:
                write_file(out_path, resp.content)

    # Copiar PT index para root index (útil para GitHub Pages onde / serve o site)
    pt_index = docs_root / 'pt' / 'index.html'
    if pt_index.exists():
        write_file(docs_root / 'index.html', pt_index.read_bytes())

    print('\nExport concluído. Verifique a pasta `docs/` e faça commit/push para GitHub.')


if __name__ == '__main__':
    main()
