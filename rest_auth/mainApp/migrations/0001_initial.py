# Generated by Django 4.2.4 on 2023-12-26 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Company",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("company_name", models.CharField(max_length=100)),
                ("location", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Employee",
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
                ("name", models.CharField(max_length=100)),
                ("salary", models.IntegerField()),
                ("email", models.EmailField(max_length=150)),
                (
                    "eid",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mainApp.company",
                    ),
                ),
            ],
        ),
    ]
