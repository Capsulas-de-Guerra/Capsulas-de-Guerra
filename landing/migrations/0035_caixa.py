# Generated by Django 3.2 on 2022-02-15 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0034_delete_caixa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Caixa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=500)),
            ],
        ),
    ]
