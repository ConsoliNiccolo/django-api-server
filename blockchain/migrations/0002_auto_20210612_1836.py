# Generated by Django 3.2.3 on 2021-06-12 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blockchain', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(
            'ALTER SEQUENCE blockchain_token_id_seq MINVALUE 0 START 0 RESTART WITH 0;'
        )
    ]
