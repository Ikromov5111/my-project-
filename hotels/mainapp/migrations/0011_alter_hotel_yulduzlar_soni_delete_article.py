# Generated by Django 4.0.3 on 2022-04-26 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_alter_hotel_yulduzlar_soni'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='yulduzlar_soni',
            field=models.CharField(choices=[('4', '4'), ('2', '2'), ('3', '3'), ('5', '5'), ('1', '1')], max_length=2),
        ),
        migrations.DeleteModel(
            name='Article',
        ),
    ]
