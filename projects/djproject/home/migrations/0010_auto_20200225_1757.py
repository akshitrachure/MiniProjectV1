# Generated by Django 2.2.3 on 2020-02-25 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20200225_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detailed_marks',
            name='FinalTotal',
            field=models.IntegerField(null=True, verbose_name='FinalTotal'),
        ),
        migrations.AlterField(
            model_name='detailed_marks',
            name='max1',
            field=models.IntegerField(null=True, verbose_name='MaxTotal1'),
        ),
        migrations.AlterField(
            model_name='detailed_marks',
            name='max2',
            field=models.IntegerField(null=True, verbose_name='MaxTotal2'),
        ),
        migrations.AlterField(
            model_name='detailed_marks',
            name='max3',
            field=models.IntegerField(null=True, verbose_name='MaxTotal3'),
        ),
        migrations.AlterField(
            model_name='detailed_marks',
            name='max4',
            field=models.IntegerField(null=True, verbose_name='MaxTotal4'),
        ),
        migrations.AlterField(
            model_name='detailed_marks',
            name='max5',
            field=models.IntegerField(null=True, verbose_name='MaxTotal5'),
        ),
        migrations.AlterField(
            model_name='detailed_marks',
            name='sub_id',
            field=models.IntegerField(null=True, verbose_name='SubjectID'),
        ),
        migrations.AlterField(
            model_name='detailed_marks',
            name='total1',
            field=models.IntegerField(null=True, verbose_name='Total1'),
        ),
        migrations.AlterField(
            model_name='detailed_marks',
            name='total10',
            field=models.IntegerField(null=True, verbose_name='Total10'),
        ),
        migrations.AlterField(
            model_name='detailed_marks',
            name='total2',
            field=models.IntegerField(null=True, verbose_name='Total2'),
        ),
        migrations.AlterField(
            model_name='detailed_marks',
            name='total3',
            field=models.IntegerField(null=True, verbose_name='Total3'),
        ),
        migrations.AlterField(
            model_name='detailed_marks',
            name='total4',
            field=models.IntegerField(null=True, verbose_name='Total4'),
        ),
        migrations.AlterField(
            model_name='detailed_marks',
            name='total5',
            field=models.IntegerField(null=True, verbose_name='Total5'),
        ),
        migrations.AlterField(
            model_name='detailed_marks',
            name='total6',
            field=models.IntegerField(null=True, verbose_name='Total6'),
        ),
        migrations.AlterField(
            model_name='detailed_marks',
            name='total7',
            field=models.IntegerField(null=True, verbose_name='Total7'),
        ),
        migrations.AlterField(
            model_name='detailed_marks',
            name='total8',
            field=models.IntegerField(null=True, verbose_name='Total8'),
        ),
        migrations.AlterField(
            model_name='detailed_marks',
            name='total9',
            field=models.IntegerField(null=True, verbose_name='Total9'),
        ),
    ]
