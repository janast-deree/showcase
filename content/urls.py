from django.contrib.sitemaps.views import sitemap
from django.urls import path

from .sitemaps import StaticSitemap
from .views import *

sitemaps = {
    'static': StaticSitemap
}

urlpatterns = [
    path('', index, name='home'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('filter_pieces', filter_pieces, name='filter_pieces'),
]