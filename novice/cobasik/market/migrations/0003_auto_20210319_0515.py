# Generated by Django 2.2 on 2021-03-19 05:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_auto_20210319_0437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrasi',
            name='kategori',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, related_name='cats', to='market.Category'),
        ),
    ]