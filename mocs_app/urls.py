from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('timeline/', views.TimelinePageView.as_view(), name='timeline'),
    path('team/', views.TeamPageView.as_view(), name='team'),
    path('partners/', views.PartnersPageView.as_view(), name='partners'),
    path('shop/', views.ShopPageView.as_view(), name='shop'),
    path('gallery/', views.GalleryPageView.as_view(), name='gallery'),
    path('blog/', views.BlogPageView.as_view(), name='blog'),
    path('blog/<int:pk>/', views.BlogPostDetailView.as_view(), name='blog_post_detail'),
    path('events/', views.EventsPageView.as_view(), name='events'),
    path('contact/', views.ContactPageView.as_view(), name='contact'),
    path('join/', views.JoinFormView.as_view(), name='join'),
]
