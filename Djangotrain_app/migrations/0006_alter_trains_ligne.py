# Generated by Django 5.0.2 on 2024-04-08 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Djangotrain_app', '0005_alter_trains_ligne'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trains',
            name='ligne',
            field=models.IntegerField(),
        ),
    ]
