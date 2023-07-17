# Generated by Django 4.2.1 on 2023-07-06 04:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("mainApp", "0007_rename_name_wishlist_product"),
    ]

    operations = [
        migrations.CreateModel(
            name="Checkout",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("total", models.IntegerField()),
                ("shipping", models.IntegerField()),
                ("final", models.IntegerField()),
                (
                    "rppid",
                    models.CharField(blank=True, default="", max_length=30, null=True),
                ),
                ("date", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="mainApp.buyer"
                    ),
                ),
            ],
        ),
    ]
