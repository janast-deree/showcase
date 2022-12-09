from django.contrib.sitemaps.views import sitemap
from django.urls import path

from .sitemaps import *
from .views import *

sitemaps = {
    'static': StaticSitemap,
    'artists': ArtistsSitemap,
    'pieces': PiecesSitemap
}

urlpatterns = [
    path('', index, name='home'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('filter_pieces', filter_pieces, name='filter_pieces'),
    path('artists/<int:pk>', artist, name='artist'),
    path('pieces/<int:pk>', piece, name='piece'),
]