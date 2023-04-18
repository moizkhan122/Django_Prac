# Generated by Django 4.2 on 2023-04-15 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0002_companymodel_about_companymodel_active_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companymodel',
            name='about',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='companymodel',
            name='location',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='companymodel',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='companymodel',
            name='type',
            field=models.CharField(choices=[(1, 'IT'), (2, 'Non IT'), (3, 'Phone Mobile')], max_length=100),
        ),
    ]
