# Generated by Django 3.2.5 on 2022-02-19 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_auto_20220220_0424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='rating',
            field=models.CharField(default='0', max_length=1),
        ),
    ]
