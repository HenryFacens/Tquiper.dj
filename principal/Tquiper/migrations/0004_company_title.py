# Generated by Django 4.1.6 on 2023-03-10 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tquiper', '0003_remove_company_company_remove_company_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
