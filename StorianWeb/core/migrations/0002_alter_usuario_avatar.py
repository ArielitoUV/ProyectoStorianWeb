# Generated by Django 4.1 on 2023-12-08 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usuario",
            name="avatar",
            field=models.CharField(
                blank=True,
                choices=[
                    ("chico.png", "Avatar Chico"),
                    ("madre.png", "Avatar Madre"),
                    ("papa.png", "Avatar Papa"),
                ],
                max_length=100,
                null=True,
            ),
        ),
    ]
