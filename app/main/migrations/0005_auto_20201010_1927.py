# Generated by Django 3.1.2 on 2020-10-10 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20201006_1929'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shorturl',
            options={'ordering': ('-created_at',)},
        ),
    ]
