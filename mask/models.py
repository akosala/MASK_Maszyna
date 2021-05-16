from django.db import models
from django.contrib.auth.models import User

# Create your models here.m
class XXX_Kontrah(models.Model):
    id_kontrahent = models.IntegerField()
    kontrahe = models.CharField(verbose_name="Kontrahent", max_length=100)
    DL_kontrahent = models.CharField(verbose_name="Kontrahent Nazwa Długa",max_length=500)

    def __str__(self):
        return self.DL_kontrahent
    class Meta:
        verbose_name = "XXX_Kontrahent"
        verbose_name_plural = "XXX_Kontrahenci"
class Pracownik(models.Model):
    #pracownik_id=models.ForeignKey(User,on_delete=models.CASCADE)
    pracownik=models.CharField(verbose_name='PracownikName',max_length=200)

class Kontrah(models.Model):
    id_kontrahent = models.IntegerField()
    kontrahe = models.CharField(verbose_name="Kontrahent", max_length=100)
    DL_kontrahent = models.CharField(verbose_name="Kontrahent Nazwa Długa",max_length=500)

    def __str__(self):
        return self.DL_kontrahent
    class Meta:
        verbose_name = "Kontrahent"
        verbose_name_plural = "Kontrahenci"

class ZUS(models.Model):

    kontrahent = models.ForeignKey(Kontrah,on_delete=models.CASCADE)
    pracownik = models.ForeignKey(User,on_delete=models.CASCADE)  #models.CharField(max_length=100)
    zus10 = models.CharField(max_length=100)
    zus15 = models.CharField(max_length=100)
    PIT_4 = models.CharField(max_length=100)
    LP = models.CharField(max_length=100)
    RACH = models.CharField(max_length=100)
    czas_realizacj = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

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
    weryfikacja_rej_Vat = models.CharField(max_length=100)
    Vat_JPK = models.CharField(max_length=100)
    czas_realizacj = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.kontrahent

    class Meta:
        verbose_name = "US"
        verbose_name_plural = "US"