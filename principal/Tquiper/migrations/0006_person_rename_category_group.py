# Generated by Django 4.1.6 on 2023-03-15 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tquiper', '0005_category_alter_company_options_alter_company_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.RenameModel(
            old_name='Category',
            new_name='Group',
        ),
    ]