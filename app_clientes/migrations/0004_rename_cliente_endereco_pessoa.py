# Generated by Django 4.1.1 on 2022-10-23 23:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_clientes', '0003_endereco'),
    ]

    operations = [
        migrations.RenameField(
            model_name='endereco',
            old_name='cliente',
            new_name='pessoa',
        ),
    ]