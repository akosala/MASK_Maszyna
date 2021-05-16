from django.db import models
from django.contrib.auth.models import User


class XXX_Kontrah(models.Model):

    id_kontrahent = models.IntegerField()
    kontrahe = models.CharField(verbose_name="Kontrahent", max_length=100)
    DL_kontrahent = models.CharField(verbose_name="Kontrahent Nazwa Długa", max_length=500)

    def __str__(self):
        return self.DL_kontrahent

    class Meta:
        verbose_name = "XXX_Kontrahent"
        verbose_name_plural = "XXX_Kontrahenci"


class Slownik1(models.Model):

    wartosc=models.CharField(verbose_name='Wartosc', max_length=50)

    def __str__(self):
        return self.wartosc

    class Meta:
        verbose_name = "Wartość"
        verbose_name_plural = "Warości"


class Slownik2(models.Model):

    wartosc=models.CharField(verbose_name='Wartosc', max_length=50)

    def __str__(self):
        return self.wartosc

    class Meta:
        verbose_name = "Wartość"
        verbose_name_plural = "Warości"


class Pracownik_pow(models.Model):

    pracownik=models.CharField(verbose_name='PracownikName', max_length=200)

    def __str__(self):
        return self.pracownik

    class Meta:
        verbose_name = "Pracownik"
        verbose_name_plural = "Pracownicy"


class Kontrah(models.Model):
    id_kontrahent = models.IntegerField()
    kontrahe = models.CharField(verbose_name="Kontrahent", max_length=100)
    DL_kontrahent = models.CharField(verbose_name="Kontrahent Nazwa Długa", max_length=500)
    pracownik_odpowiedzialnv = models.ForeignKey(Pracownik_pow, on_delete=models.CASCADE)

    def __str__(self):
        return self.DL_kontrahent

    class Meta:
        verbose_name = "Kontrahent"
        verbose_name_plural = "Kontrahenci"


class ZUS(models.Model):

    kontrahent = models.ForeignKey(Kontrah,on_delete=models.CASCADE)
    pracownik = models.ForeignKey(User,on_delete=models.CASCADE)
    zus10 = models.CharField(max_length=100)
    zus15 = models.CharField(max_length=100)
    PIT_4 = models.CharField(max_length=100)
    LP = models.ForeignKey(Slownik1,on_delete=models.CASCADE)
    RACH = models.ForeignKey(Slownik2,on_delete=models.CASCADE)
    czas_realizacj = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    data_obowiazywania = models.DateField()

    def __str__(self):

        return self.kontrahent

    class Meta:
        verbose_name = "ZUS"
        verbose_name_plural = "ZUS"


class US(models.Model):

    kontrahent = models.ForeignKey(Kontrah,on_delete=models.CASCADE)
    pracownik = models.ForeignKey(User,on_delete=models.CASCADE)
    ilosc_dokumentow = models.IntegerField()
    okres_Pit_Cit = models.CharField(max_length=100)
    okres_Vat = models.CharField(max_length=100)
    weryfikacja_rej_Vat = models.ForeignKey(Slownik1,on_delete=models.CASCADE)
    Vat_JPK = models.CharField(max_length=100)
    czas_realizacj = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    data_obowiazywania = models.DateField()

    def __str__(self):
        return self.kontrahent

    class Meta:
        verbose_name = "US"
        verbose_name_plural = "US"