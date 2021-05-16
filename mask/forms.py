from django import forms
from .models import ZUS, US


class ZusForm(forms.ModelForm):
    class Meta:
        model = ZUS
        fields = ('kontrahent','zus10', 'zus15', 'PIT_4', 'LP', 'RACH', 'czas_realizacj')


class UsForm(forms.ModelForm):
    class Meta:
        model = US
        fields = ('kontrahent', 'ilosc_dokumentow', 'okres_Pit_Cit'
                 , 'okres_Vat', 'weryfikacja_rej_Vat', 'Vat_JPK', 'czas_realizacj')
