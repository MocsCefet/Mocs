from django.db import models
from django.utils.translation import gettext_lazy as _

# Modelo para Membros da Equipe
class TeamMember(models.Model):
    name = models.CharField(_("Nome"), max_length=100)
    role = models.CharField(_("Cargo"), max_length=100)
    bio = models.TextField(_("Bio Curta"), blank=True)
    photo = models.ImageField(_("Foto"), upload_to='team_photos/', blank=True, null=True,
                              help_text=_("Use uma foto 400x400. Use placehold.co para placeholders."))

    def __str__(self):
        return self.name

# Modelo para Parceiros
class Partner(models.Model):
    name = models.CharField(_("Nome"), max_length=100)
    logo = models.ImageField(_("Logo"), upload_to='partner_logos/', blank=True, null=True)
    website_url = models.URLField(_("Website"), blank=True)

    def __str__(self):
        return self.name

# Modelo para Produtos da Loja (Pins, Broches)
class Product(models.Model):
    name = models.CharField(_("Nome do Produto"), max_length=100)
    description = models.TextField(_("Descrição"))
    price = models.DecimalField(_("Preço (R$)"), max_digits=6, decimal_places=2)
    image = models.ImageField(_("Imagem"), upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.name

# Modelo para Galeria de Fotos
class GalleryImage(models.Model):
    CATEGORY_CHOICES = [
        ('evento', _('Eventos')),
        ('bastidores', _('Bastidores')),
        ('produto', _('Produtos')),
    ]
    title = models.CharField(_("Título/Descrição"), max_length=200, blank=True)
    category = models.CharField(_("Categoria"), max_length=50, choices=CATEGORY_CHOICES, default='evento')
    image = models.ImageField(_("Imagem"), upload_to='gallery/')

    def __str__(self):
        return self.title or f"Imagem {self.id}"

# Modelo para Notícias (Blog)
class Post(models.Model):
    title = models.CharField(_("Título"), max_length=200)
    content = models.TextField(_("Conteúdo"))
    published_date = models.DateTimeField(_("Data de Publicação"), auto_now_add=True)

    def __str__(self):
        return self.title

# Modelo para Eventos
class Event(models.Model):
    TYPE_CHOICES = [
        ('aberto', _('Aberto')),
        ('exclusivo', _('Exclusivo (Alunos CEFET-MG)')),
        ('quinzenal', _('Encontro Quinzenal')),
    ]
    title = models.CharField(_("Título"), max_length=200)
    description = models.TextField(_("Descrição"))
    event_date = models.CharField(_("Data (texto)"), max_length=100, help_text=_("Ex: 'Maio 2025' ou 'Toda 1ª e 3ª Sexta'"))
    event_type = models.CharField(_("Tipo"), max_length=50, choices=TYPE_CHOICES, default='aberto')
    delegates_expected = models.CharField(_("Delegados"), max_length=50, blank=True, help_text=_("Ex: '200+' ou '50'"))
    registration_open = models.BooleanField(_("Inscrições Abertas"), default=False)
    registration_url = models.URLField(_("Link de Inscrição"), blank=True)

    def __str__(self):
        return self.title

# Modelo para Formulários de Interesse
class JoinInterest(models.Model):
    FORM_TYPE_CHOICES = [
        ('equipe', _('Equipe')),
        ('diretor', _('Diretor de Comitê')),
    ]
    form_type = models.CharField(_("Tipo de Formulário"), max_length=50, choices=FORM_TYPE_CHOICES)
    name = models.CharField(_("Nome"), max_length=100)
    email = models.EmailField(_("E-mail"))
    phone = models.CharField(_("Telefone"), max_length=20, blank=True)
    course_year = models.CharField(_("Curso/Ano/Instituição"), max_length=200)
    motivation = models.TextField(_("Motivação"))
    experience = models.TextField(_("Experiência Prévia"), blank=True)
    cv = models.FileField(_("CV (Opcional)"), upload_to='cvs/', blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.get_form_type_display()}"
