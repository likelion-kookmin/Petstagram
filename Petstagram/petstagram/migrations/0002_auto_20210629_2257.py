# Generated by Django 3.2.4 on 2021-06-29 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petstagram', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='create_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='feed',
            name='writer',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
