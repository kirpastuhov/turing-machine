# Generated by Django 2.0.2 on 2018-05-19 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machine', '0005_auto_20180519_0624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='step',
            name='step',
            field=models.IntegerField(default=1),
        ),
    ]
