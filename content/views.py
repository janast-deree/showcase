from django.shortcuts import render
from content.models import Piece, Artist, Art


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
            except ValueError:
                pass
            try:
                if 'artist' in request.POST:
                    artist_id = int(request.POST['artist'])
                    pieces = pieces.filter(artists__pk=artist_id)
            except ValueError:
                pass
        else:
            pieces = pieces.filter(public=True)
        return render(request, 'content/pieces.html', {
            'pieces': pieces
        })
