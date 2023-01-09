# Generated by Django 4.1.5 on 2023-01-09 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0004_remove_room_room_reservations'),
        ('users', '0004_alter_reservations_users_rooms_checkin_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='reservations',
            field=models.ManyToManyField(related_name='reservations', through='users.Reservations_users_rooms', to='rooms.room'),
        ),
    ]