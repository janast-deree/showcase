from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render
from content.models import Piece, Artist, Art
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def index(request):
    context = {
        'pieces': Piece.objects.all(),
    }
    if request.user.is_authenticated:
        context['artists'] = Artist.objects.all()
        context['categories'] = Art.objects.all()
    else:
        context['pieces'] = context['pieces'].filter(public=True)
    return render(request, 'content/index.html', context)

@login_required
def artist(request, **kwargs):
    try:
        artist_obj = Artist.objects.get(pk=kwargs['pk'])
        return render(request, 'content/artist.html', {'artist': artist_obj})
    except ObjectDoesNotExist as e:
        raise Http404


@login_required
def piece(request, **kwargs):
    try:
        piece_obj = Piece.objects.get(pk=kwargs['pk'])
        return render(request, 'content/piece.html', {'piece': piece_obj})
    except ObjectDoesNotExist as e:
        raise Http404


def filter_pieces(request):
    if request.method == 'POST':
        pieces = Piece.objects.all()
        if 'name' in request.POST and len(request.POST['name']) >= 3:
            pieces = pieces.filter(name__contains=request.POST['name'])
        if request.user.is_authenticated:
            try:
                if 'category' in request.POST:
                    category_id = int(request.POST['category'])
                    pieces = pieces.filter(artists__art_id=category_id)
                    try:
                        if 'artist' in request.POST:
                            artist_id = int(request.POST['artist'])
                            pieces = pieces.filter(artists__pk=artist_id)
                    except ValueError:
                        pass
            except ValueError:
                pass
        else:
            pieces = pieces.filter(public=True)
        return render(request, 'content/pieces.html', {
            'pieces': pieces
        })
