from django.contrib import admin
from .models import (
    TeamMember, Partner, Product, GalleryImage, Post, Event, JoinInterest
)


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role')


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'website_url')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    list_filter = ('category',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'event_date', 'event_type', 'registration_open')
    list_filter = ('event_type', 'registration_open')


@admin.register(JoinInterest)
class JoinInterestAdmin(admin.ModelAdmin):
    list_display = ('name', 'form_type', 'email', 'submitted_at')
    list_filter = ('form_type',)
    readonly_fields = ('submitted_at',)
