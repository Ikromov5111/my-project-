# Generated by Django 4.0.3 on 2022-04-05 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_alter_hotel_yulduzlar_soni'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='yulduzlar_soni',
            field=models.CharField(choices=[('2', '2'), ('3', '3'), ('1', '1'), ('5', '5'), ('4', '4')], max_length=2),
        ),
        migrations.AlterField(
            model_name='worker',
            name='added_time',
            field=models.DateField(auto_now_add=True),
        ),
    ]
