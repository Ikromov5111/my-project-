# Generated by Django 4.0.3 on 2022-04-08 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_alter_article_photo_alter_hotel_yulduzlar_soni'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='yulduzlar_soni',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('5', '5'), ('4', '4')], max_length=2),
        ),
    ]