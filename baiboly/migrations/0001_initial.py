# Generated by Django 4.2.3 on 2023-09-27 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="cls_baibl",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("bible", models.CharField(max_length=30)),
                ("type_bible", models.CharField(max_length=30)),
                ("nbr_chapitre", models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name="vrs_baibl",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("chptr", models.IntegerField()),
                (
                    "bible_vrs",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="baiboly.cls_baibl",
                    ),
                ),
            ],
        ),
    ]
