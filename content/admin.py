from django.contrib import admin
from .models import Art, Artist, Piece


# Register your models here.
class PieceAdmin(admin.ModelAdmin):
    filter_horizontal = ['artists']


admin.site.register(Art)
admin.site.register(Artist)
admin.site.register(Piece, PieceAdmin)
