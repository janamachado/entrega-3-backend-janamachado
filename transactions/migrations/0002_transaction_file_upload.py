# Generated by Django 4.1.5 on 2023-01-27 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("transactions", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="transaction",
            name="file_upload",
            field=models.FileField(default="Pesquise por um arquivo", upload_to=""),
        ),
    ]
