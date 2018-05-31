from django.shortcuts import render
from .translate import change

# Create your views here.


def translation_view(request):
    """Translate and render translation."""
    if request.method == 'POST':
        context = {}

        original = request.POST['translate-text']
        new = change(original)

        context['original'] = original
        context['new'] = new

        return render(request, 'translation.html', context)
