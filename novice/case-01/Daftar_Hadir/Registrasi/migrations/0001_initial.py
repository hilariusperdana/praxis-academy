# Generated by Django 2.2 on 2021-02-23 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registrasi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_urut', models.CharField(max_length=10)),
                ('nama', models.CharField(max_length=255)),
                ('jam_hadir', models.CharField(max_length=255)),
                ('no_tlp', models.CharField(max_length=15)),
            ],
        ),
    ]
