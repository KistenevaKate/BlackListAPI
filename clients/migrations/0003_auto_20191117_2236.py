# Generated by Django 2.2.7 on 2019-11-17 19:36

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_auto_20191117_1831'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientsContacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Доп. контакт клиента',
                'verbose_name_plural': 'Доп. контакты клиентов',
            },
        ),
        migrations.CreateModel(
            name='ContactType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Вид контактных данных',
                'verbose_name_plural': 'Виды контактных данных',
            },
        ),
        migrations.AlterModelOptions(
            name='clients',
            options={'verbose_name': 'Клиент', 'verbose_name_plural': 'Клиенты'},
        ),
        migrations.AddField(
            model_name='clients',
            name='email',
            field=models.CharField(max_length=50, null=True, verbose_name='Электронная почта'),
        ),
        migrations.AddField(
            model_name='clients',
            name='phone',
            field=models.CharField(max_length=20, null=True, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='about',
            field=models.TextField(null=True, verbose_name='Заметка о контакте'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Когда создан'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='firstName',
            field=models.CharField(max_length=100, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='lastName',
            field=models.CharField(max_length=100, verbose_name='Фамилия'),
        ),
        migrations.DeleteModel(
            name='ClientsPhone',
        ),
        migrations.DeleteModel(
            name='Phone',
        ),
        migrations.AddField(
            model_name='clientscontacts',
            name='clients',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.Clients'),
        ),
        migrations.AddField(
            model_name='clientscontacts',
            name='contactType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.ContactType'),
        ),
    ]
