# Generated by Django 5.1 on 2024-08-18 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wikiApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tituloArticulo', models.CharField(blank=True, max_length=48, null=True)),
                ('nombreTema', models.CharField(blank=True, max_length=48, null=True)),
                ('contenidoArticulo', models.CharField(blank=True, max_length=256, null=True)),
            ],
        ),
    ]
