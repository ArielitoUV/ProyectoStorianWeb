# Generated by Django 4.1 on 2023-11-17 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tabla_test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('columna_uno', models.CharField(max_length=200)),
                ('columna_dos', models.CharField(max_length=200)),
                ('columna_tres', models.CharField(max_length=200)),
                ('columna_cuatro', models.CharField(max_length=200)),
            ],
        ),
    ]
