# Generated by Django 4.1.5 on 2023-01-05 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adresses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='cep',
            field=models.CharField(default=0, max_length=9),
            preserve_default=False,
        ),
    ]
