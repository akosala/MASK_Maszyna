# Generated by Django 3.1.7 on 2021-05-18 17:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Kontrah',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_kontrahent', models.IntegerField()),
                ('kontrahe', models.CharField(max_length=100, verbose_name='Kontrahent')),
                ('DL_kontrahent', models.CharField(max_length=500, verbose_name='Kontrahent Nazwa Długa')),
            ],
            options={
                'verbose_name': 'Kontrahent',
                'verbose_name_plural': 'Kontrahenci',
            },
        ),
        migrations.CreateModel(
            name='OkresRozrachunkowy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('miesiac', models.CharField(max_length=50, verbose_name='miesiac')),
            ],
            options={
                'verbose_name': 'Okres Rozrachunkowy',
                'verbose_name_plural': 'Okresy Rozrachunkowe',
            },
        ),
        migrations.CreateModel(
            name='Pracownik_pow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pracownik', models.CharField(max_length=200, verbose_name='PracownikName')),
            ],
            options={
                'verbose_name': 'Pracownik Powiązany',
                'verbose_name_plural': 'Pracownicy Powiązani',
            },
        ),
        migrations.CreateModel(
            name='Slownik1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wartosc', models.CharField(max_length=50, verbose_name='Wartosc')),
            ],
            options={
                'verbose_name': 'Slownik1',
                'verbose_name_plural': 'Slownik1',
            },
        ),
        migrations.CreateModel(
            name='Slownik2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wartosc', models.CharField(max_length=50, verbose_name='Wartosc')),
            ],
            options={
                'verbose_name': 'Slownik2',
                'verbose_name_plural': 'Slownik2',
            },
        ),
        migrations.CreateModel(
            name='XXX_Kontrah',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_kontrahent', models.IntegerField()),
                ('kontrahe', models.CharField(max_length=100, verbose_name='Kontrahent')),
                ('DL_kontrahent', models.CharField(max_length=500, verbose_name='Kontrahent Nazwa Długa')),
            ],
            options={
                'verbose_name': 'XXX_Kontrahent',
                'verbose_name_plural': 'XXX_Kontrahenci',
            },
        ),
        migrations.CreateModel(
            name='ZUS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zus10', models.CharField(max_length=100)),
                ('zus15', models.CharField(max_length=100)),
                ('PIT_4', models.CharField(max_length=100)),
                ('czas_realizacj', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('LP', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mask.slownik1')),
                ('RACH', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mask.slownik2')),
                ('kontrahent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mask.kontrah')),
                ('miesiac', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mask.okresrozrachunkowy')),
                ('pracownik', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'ZUS',
                'verbose_name_plural': 'ZUS',
            },
        ),
        migrations.CreateModel(
            name='US',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ilosc_dokumentow', models.IntegerField()),
                ('okres_Pit_Cit', models.CharField(max_length=100)),
                ('okres_Vat', models.CharField(max_length=100)),
                ('Vat_JPK', models.CharField(max_length=100)),
                ('czas_realizacj', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('kontrahent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mask.kontrah', verbose_name='Kontrahenr')),
                ('miesiac', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mask.okresrozrachunkowy')),
                ('pracownik', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('weryfikacja_rej_Vat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mask.slownik1')),
            ],
            options={
                'verbose_name': 'US',
                'verbose_name_plural': 'US',
            },
        ),
        migrations.AddField(
            model_name='kontrah',
            name='pracownik_odpowiedzialnv',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mask.pracownik_pow'),
        ),
    ]
