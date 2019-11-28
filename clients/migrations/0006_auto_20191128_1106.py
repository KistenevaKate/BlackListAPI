# Generated by Django 2.2.7 on 2019-11-28 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0005_auto_20191128_1056'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment_client',
            options={'verbose_name': 'Статус клиента', 'verbose_name_plural': 'Статусы клиентов'},
        ),
        migrations.AlterModelOptions(
            name='status_client',
            options={'verbose_name': 'Статус клиента', 'verbose_name_plural': 'Статусы клиентов'},
        ),
        migrations.RenameField(
            model_name='client',
            old_name='id_status_client',
            new_name='status_client',
        ),
        migrations.RenameField(
            model_name='comment_client',
            old_name='id_client',
            new_name='client',
        ),
        migrations.RenameField(
            model_name='comment_client',
            old_name='id_user',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='comment_client',
            name='id_status_client',
        ),
    ]
