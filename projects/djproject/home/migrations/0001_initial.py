# Generated by Django 2.2.2 on 2019-08-05 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='subjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_code', models.CharField(choices=[('CSE', 'Computer Science'), ('MH', 'Mech'), ('CV', 'Civil'), ('ISE', 'Information Science'), ('EC', 'Electronics and Communication'), ('EEE', 'Electronics and Electrical'), ('TC', 'Telecommunication')], max_length=10, verbose_name='Subject Code')),
                ('sub_name', models.CharField(max_length=50, verbose_name='Subject Name')),
                ('semester', models.CharField(max_length=2, verbose_name='Semester')),
            ],
        ),
    ]
