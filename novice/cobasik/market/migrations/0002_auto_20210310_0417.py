# Generated by Django 2.2 on 2021-03-10 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registrasi',
            old_name='alamat',
            new_name='deskripsi',
        ),
        migrations.RemoveField(
            model_name='registrasi',
            name='no_urut',
        ),
        migrations.AddField(
            model_name='registrasi',
            name='harga',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
    ]
