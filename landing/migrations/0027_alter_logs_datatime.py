# Generated by Django 3.2 on 2022-01-31 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0026_logs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logs',
            name='datatime',
            field=models.CharField(max_length=500),
        ),
    ]
