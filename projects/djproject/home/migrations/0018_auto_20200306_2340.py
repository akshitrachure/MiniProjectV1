# Generated by Django 2.2.3 on 2020-03-06 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_auto_20200306_2337'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='generatebarcode',
            name='semid',
        ),
        migrations.AddField(
            model_name='generatebarcode',
            name='sem_id',
            field=models.IntegerField(null=True, verbose_name='SemesterID'),
        ),
    ]
