# Generated by Django 4.2.7 on 2023-11-19 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("fihirana", "0006_list_fihirana_ajout_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="list_fihirana_ajout",
            name="Titre",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="fihirana.fhrn_ajout"
            ),
        ),
    ]
