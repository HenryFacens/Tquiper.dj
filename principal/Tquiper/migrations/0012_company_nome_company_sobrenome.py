# Generated by Django 4.1.6 on 2023-04-07 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tquiper', '0011_rename_datetimefield_company_updated_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='Nome',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='company',
            name='Sobrenome',
            field=models.CharField(default='', max_length=100),
        ),
    ]
