from django import forms
from django.utils.translation import gettext as _

class SpeedForm(forms.Form):
    domain = forms.CharField(label=_("dominio"), max_length=100,
            widget=forms.TextInput(attrs={'placeholder': _("dominio o IP")}))

