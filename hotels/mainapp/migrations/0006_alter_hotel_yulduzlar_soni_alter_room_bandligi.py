# Generated by Django 4.0.3 on 2022-04-06 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_alter_hotel_yulduzlar_soni_alter_worker_added_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='yulduzlar_soni',
            field=models.CharField(choices=[('4', '4'), ('5', '5'), ('1', '1'), ('2', '2'), ('3', '3')], max_length=2),
        ),
        migrations.AlterField(
            model_name='room',
            name='bandligi',
            field=models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], max_length=15),
        ),
    ]
