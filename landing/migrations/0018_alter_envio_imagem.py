# Generated by Django 3.2 on 2022-01-03 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0017_alter_envio_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='envio',
            name='imagem',
            field=models.TextField(),
        ),
    ]
