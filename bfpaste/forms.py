from django import forms

from .utils import SUPPORT_LANGS
from .models import Paste


class PasteForm(forms.ModelForm):
    class Meta:
        model = Paste
        fields = ['author', 'content', 'lang']
        exclude = ['paste_id']
        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control w-25',
                                             'autocomplete': 'off',
                                             'spellcheck': 'false',
                                             }),
            'content': forms.Textarea(attrs={'class': 'form-control consolas',
                                             'autocomplete': 'off',
                                             'spellcheck': 'false',
                                             'rows': 20}),

            'lang': forms.Select(attrs={'class': 'form-control'})
        }
