# Generated by Django 4.0.3 on 2022-03-29 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('room_qty', models.PositiveIntegerField()),
                ('ochilgan_sana', models.DateField(null=True)),
                ('yulduzlar_soni', models.CharField(choices=[(4, 4), (5, 5), (3, 3), (2, 2), (1, 1)], max_length=1)),
                ('telefon_raqam', models.CharField(max_length=16)),
                ('qushimcha_malumot', models.TextField()),
                ('added_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('birth_date', models.DateField()),
                ('phone', models.CharField(max_length=18)),
                ('pasport_serias', models.CharField(max_length=9)),
                ('email', models.EmailField(max_length=254)),
                ('adress', models.CharField(max_length=60)),
                ('added_time', models.DateField(auto_now=True)),
                ('status_worker', models.CharField(choices=[('admin', 'admin'), ('menager', 'menager'), ('cooking', 'cooling'), ('one', 'one'), ('tue', 'tue')], max_length=9)),
            ],
        ),
    ]
