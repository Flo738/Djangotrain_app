# Generated by Django 5.0.2 on 2024-04-01 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trains',
            fields=[
                ('trainId', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('destination', models.CharField(max_length=50)),
                ('overview', models.CharField(max_length=200)),
            ],
        ),
    ]