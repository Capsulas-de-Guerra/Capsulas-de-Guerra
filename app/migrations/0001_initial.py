# Generated by Django 3.2 on 2021-12-12 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Experiment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hash', models.TextField(blank=True)),
                ('lote', models.TextField(blank=True)),
                ('file', models.FileField(blank=True, default='', upload_to='')),
                ('user', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Imagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagens', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
