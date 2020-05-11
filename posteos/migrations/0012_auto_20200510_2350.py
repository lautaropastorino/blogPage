# Generated by Django 3.0.5 on 2020-05-11 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posteos', '0011_mail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mail',
            name='dierccion',
        ),
        migrations.AddField(
            model_name='mail',
            name='direccion',
            field=models.EmailField(default='default@example.com', max_length=254, unique=True),
            preserve_default=False,
        ),
    ]