from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView
from .models import TeamMember, Partner, Product, GalleryImage, Post, Event


class HomePageView(ListView):
    template_name = 'index.html'
    context_object_name = 'upcoming_events'
    queryset = Event.objects.all().order_by('-event_date')[:2]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gallery_preview'] = GalleryImage.objects.all()[:4]
        return context


class AboutPageView(TemplateView):
    template_name = 'about.html'


class TimelinePageView(TemplateView):
    template_name = 'timeline.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['timeline_data'] = [
            {"year": "2010", "title": "Fundação", "desc": "O MOCS é fundado no CEFET-MG..."},
            {"year": "2014", "title": "MOCS IV", "desc": "Consolidação do evento..."},
            {"year": "2019", "title": "Expansão", "desc": "Início dos projetos 'MOCS em Sala'..."},
            {"year": "2024", "title": "Retomada", "desc": "Planejamento da MOCS XII..."},
            {"year": "2025", "title": "MOCS XII", "desc": "A maior edição planejada..."},
        ]
        return context


class TeamPageView(ListView):
    model = TeamMember
    template_name = 'team.html'
    context_object_name = 'team_members'


class PartnersPageView(ListView):
    model = Partner
    template_name = 'partners.html'
    context_object_name = 'partners'


class ShopPageView(ListView):
    model = Product
    template_name = 'shop.html'
    context_object_name = 'products'


class GalleryPageView(ListView):
    model = GalleryImage
    template_name = 'gallery.html'
    context_object_name = 'gallery_images'


class BlogPageView(ListView):
    model = Post
    template_name = 'blog.html'
    context_object_name = 'posts'
    queryset = Post.objects.all().order_by('-published_date')


class BlogPostDetailView(DetailView):
    model = Post
    template_name = 'blog_post_detail.html'
    context_object_name = 'post'


class EventsPageView(ListView):
    model = Event
    template_name = 'events.html'
    context_object_name = 'events'
    queryset = Event.objects.all().order_by('event_date')


class ContactPageView(TemplateView):
    template_name = 'contact.html'

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, {'message_sent': True})


class JoinFormView(TemplateView):
    template_name = 'join_form.html'

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form_submitted': True})
