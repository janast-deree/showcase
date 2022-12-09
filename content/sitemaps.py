from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from content.models import Piece, Artist


class StaticSitemap(Sitemap):
    changefreq = "yearly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return ['home']  # , 'login', 'register', 'admin:index', 'profile']

    def location(self, item):
        return reverse(item)


class PiecesSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'http'

    def items(self):
        return Piece.objects.all()

    def location(self, obj):
        return '/pieces/%s' % obj.id


class ArtistsSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'http'

    def items(self):
        return Artist.objects.all()

    def location(self, obj):
        return '/artists/%s' % obj.id
