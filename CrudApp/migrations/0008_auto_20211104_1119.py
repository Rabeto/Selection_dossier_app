# Generated by Django 3.1.2 on 2021-11-04 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CrudApp', '0007_auto_20211104_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidat',
            name='Note_ANG',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='candidat',
            name='Note_FR',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='candidat',
            name='Note_HG',
            field=models.IntegerField(),
        ),
    ]
