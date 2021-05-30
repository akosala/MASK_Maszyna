from django import forms
from .models import ZUS, US



class ZusForm(forms.ModelForm):

    class Meta:
        model = ZUS
        fields = ('kontrahent','zus10', 'zus15', 'PIT_4', 'LP', 'RACH', 'czas_realizacj','miesiac')

        labels ={'kontrahent':'Kontrahent :',
                  'zus10':'ZUS 10 :',
                 'zus15':'ZUS 15 : ',
                 'PIT_4': 'PIT 4 :',
                 'LP':'LP :',
                 'RACH':'RACH',
                 'czas_realizacj': 'Cazs Reaklizacji',
                 'miesiac': 'Miesiąc'}

class UsForm(forms.ModelForm):
    class Meta:
        model = US
        fields = ('kontrahent', 'ilosc_dokumentow', 'okres_Pit_Cit'
                 , 'okres_Vat', 'weryfikacja_rej_Vat', 'Vat_JPK', 'czas_realizacj','miesiac')
        labels = {'kontrahent':'Kontrahent :','ilosc_dokumentow':'Ilość Dokumentów :','okres_Pit_Cit':'Okres Piy i Cit :'
                  , 'okres_Vat':' Okres Vat ', 'weryfikacja_rej_Vat':' Weryfikacja Vat', 'Vat_JPK':'Vat JPK', 'czas_realizacj':'Czas Realizacji', 'miesiac':'Miesiąc'}


class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )
