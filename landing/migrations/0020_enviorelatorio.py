# Generated by Django 3.2 on 2022-01-11 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0019_alter_landing_imagem'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnvioRelatorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=500)),
                ('dataHora', models.DateTimeField()),
                ('documentoDigitalizado', models.IntegerField()),
            ],
        ),
    ]