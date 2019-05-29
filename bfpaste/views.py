from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from .models import Paste
from .forms import PasteForm


def index(request):
    if request.method == 'POST':
        form = PasteForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            newpaste = Paste(**data)
            newpaste.save()

            return redirect('bfpaste:show_paste', paste_id=newpaste.paste_id)
    else:
        form = PasteForm()

    return render(request, 'bfpaste/index.html', {'form': form})


def show_paste(request, paste_id):
    paste = get_object_or_404(Paste, paste_id=paste_id)

    return render(request, 'bfpaste/paste.html', context={'paste': paste})
