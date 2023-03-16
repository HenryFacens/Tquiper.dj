# Generated by Django 4.1.6 on 2023-03-15 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tquiper', '0007_empre_delete_person_alter_company_options_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Empre',
        ),
        migrations.AddField(
            model_name='company',
            name='first_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='company',
            name='last_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='company',
            name='perm',
            field=models.CharField(choices=[('admin', 'Administrador'), ('employee', 'Funcionario'), ('Company', 'Company')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='pro_imag',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
