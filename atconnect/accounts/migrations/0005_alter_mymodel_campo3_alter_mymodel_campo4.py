# Generated by Django 4.1.7 on 2023-02-18 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0004_mymodel"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mymodel",
            name="campo3",
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name="mymodel",
            name="campo4",
            field=models.CharField(max_length=10),
        ),
    ]
