# Generated by Django 2.2.7 on 2019-11-25 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_auto_20191117_2236'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clients',
            name='about',
        ),
        migrations.RemoveField(
            model_name='clients',
            name='author',
        ),
        migrations.RemoveField(
            model_name='clients',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='clients',
            name='email',
        ),
        migrations.RemoveField(
            model_name='clients',
            name='firstName',
        ),
        migrations.RemoveField(
            model_name='clients',
            name='lastName',
        ),
        migrations.RemoveField(
            model_name='clients',
            name='phone',
        ),
        migrations.DeleteModel(
            name='ClientsContacts',
        ),
        migrations.DeleteModel(
            name='ContactType',
        ),
    ]