# Generated by Django 4.2.1 on 2023-07-14 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainApp", "0011_contact"),
    ]

    operations = [
        migrations.AddField(
            model_name="buyer",
            name="otp",
            field=models.IntegerField(default=-1115555),
        ),
    ]
