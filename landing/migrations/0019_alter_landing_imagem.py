# Generated by Django 3.2 on 2022-01-11 00:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0018_alter_envio_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landing',
            name='imagem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='landing.imagem'),
        ),
    ]
