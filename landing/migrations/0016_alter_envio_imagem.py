# Generated by Django 3.2 on 2022-01-03 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0015_alter_envio_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='envio',
            name='imagem',
            field=models.CharField(max_length=50000),
        ),
    ]
