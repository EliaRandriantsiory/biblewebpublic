# Generated by Django 4.2.3 on 2023-09-27 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("baiboly", "0003_trad_chpt"),
    ]

    operations = [
        migrations.AlterField(
            model_name="vrs_baibl",
            name="bible_vrs",
            field=models.CharField(max_length=30),
        ),
    ]
