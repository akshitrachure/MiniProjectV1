# Generated by Django 2.2.3 on 2020-02-24 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_questionpaperdetails_slno'),
    ]

    operations = [
        migrations.CreateModel(
            name='detailed_marks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentid', models.IntegerField(verbose_name='StudentID')),
                ('semid', models.IntegerField(verbose_name='SemID')),
                ('sub_id', models.IntegerField(verbose_name='SubjectID')),
                ('a1', models.IntegerField(null=True, verbose_name='1a')),
                ('b1', models.IntegerField(null=True, verbose_name='1b')),
                ('c1', models.IntegerField(null=True, verbose_name='1c')),
                ('d1', models.IntegerField(null=True, verbose_name='1d')),
                ('total1', models.IntegerField(null=True, verbose_name='Total1')),
                ('a2', models.IntegerField(null=True, verbose_name='2a')),
                ('b2', models.IntegerField(null=True, verbose_name='2b')),
                ('c2', models.IntegerField(null=True, verbose_name='2c')),
                ('d2', models.IntegerField(null=True, verbose_name='2d')),
                ('total2', models.IntegerField(null=True, verbose_name='Total2')),
                ('max1', models.IntegerField(null=True, verbose_name='MaxTotal1')),
                ('a3', models.IntegerField(null=True, verbose_name='3a')),
                ('b3', models.IntegerField(null=True, verbose_name='3b')),
                ('c3', models.IntegerField(null=True, verbose_name='3c')),
                ('d3', models.IntegerField(null=True, verbose_name='3d')),
                ('total3', models.IntegerField(null=True, verbose_name='Total3')),
                ('a4', models.IntegerField(null=True, verbose_name='4a')),
                ('b4', models.IntegerField(null=True, verbose_name='4b')),
                ('c4', models.IntegerField(null=True, verbose_name='4c')),
                ('d4', models.IntegerField(null=True, verbose_name='4d')),
                ('total4', models.IntegerField(null=True, verbose_name='Total4')),
                ('max2', models.IntegerField(null=True, verbose_name='MaxTotal2')),
                ('a5', models.IntegerField(null=True, verbose_name='5a')),
                ('b5', models.IntegerField(null=True, verbose_name='5b')),
                ('c5', models.IntegerField(null=True, verbose_name='5c')),
                ('d5', models.IntegerField(null=True, verbose_name='5d')),
                ('total5', models.IntegerField(null=True, verbose_name='Total5')),
                ('a6', models.IntegerField(null=True, verbose_name='6a')),
                ('b6', models.IntegerField(null=True, verbose_name='6b')),
                ('c6', models.IntegerField(null=True, verbose_name='6c')),
                ('d6', models.IntegerField(null=True, verbose_name='6d')),
                ('total6', models.IntegerField(null=True, verbose_name='Total6')),
                ('max3', models.IntegerField(null=True, verbose_name='MaxTotal3')),
                ('a7', models.IntegerField(null=True, verbose_name='7a')),
                ('b7', models.IntegerField(null=True, verbose_name='7b')),
                ('c7', models.IntegerField(null=True, verbose_name='7c')),
                ('d7', models.IntegerField(null=True, verbose_name='7d')),
                ('total7', models.IntegerField(null=True, verbose_name='Total7')),
                ('a8', models.IntegerField(null=True, verbose_name='8a')),
                ('b8', models.IntegerField(null=True, verbose_name='8b')),
                ('c8', models.IntegerField(null=True, verbose_name='8c')),
                ('d8', models.IntegerField(null=True, verbose_name='8d')),
                ('total8', models.IntegerField(null=True, verbose_name='Total8')),
                ('max4', models.IntegerField(null=True, verbose_name='MaxTotal4')),
                ('a9', models.IntegerField(null=True, verbose_name='9a')),
                ('b9', models.IntegerField(null=True, verbose_name='9b')),
                ('c9', models.IntegerField(null=True, verbose_name='9c')),
                ('d9', models.IntegerField(null=True, verbose_name='9d')),
                ('total9', models.IntegerField(null=True, verbose_name='Total9')),
                ('a10', models.IntegerField(null=True, verbose_name='10a')),
                ('b10', models.IntegerField(null=True, verbose_name='10b')),
                ('c10', models.IntegerField(null=True, verbose_name='10c')),
                ('d10', models.IntegerField(null=True, verbose_name='10d')),
                ('total10', models.IntegerField(null=True, verbose_name='Total10')),
                ('max5', models.IntegerField(null=True, verbose_name='MaxTotal5')),
                ('final', models.IntegerField(null=True, verbose_name='FinalTotal')),
            ],
        ),
        migrations.CreateModel(
            name='generatebarcode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semid', models.IntegerField(null=True, verbose_name='SemesterID')),
                ('studentid', models.IntegerField(null=True, verbose_name='StudentID')),
                ('courseid', models.IntegerField(null=True, verbose_name='CourseID')),
                ('sub_id', models.IntegerField(null=True, verbose_name='SubjectID')),
                ('empgrp', models.IntegerField(null=True, verbose_name='EmpGroup')),
                ('Barcode', models.CharField(max_length=10, null=True, verbose_name='Barcode')),
                ('create_date', models.DateField(verbose_name='Created_date')),
                ('modif_date', models.DateField(verbose_name='Modified_date')),
                ('create_by', models.IntegerField(verbose_name='Create_By')),
                ('modified_by', models.IntegerField(verbose_name='Modified_by')),
                ('print_status', models.IntegerField(null=True, verbose_name='Print_Status')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_studentmarks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semid', models.IntegerField(null=True, verbose_name='SemesterID')),
                ('studentid', models.IntegerField(null=True, verbose_name='StudentID')),
                ('courseid', models.IntegerField(null=True, verbose_name='CourseID')),
                ('sub_id', models.IntegerField(null=True, verbose_name='SubjectID')),
                ('ia_awarded', models.IntegerField(null=True, verbose_name='IAAwarded')),
                ('ia_passfail', models.IntegerField(verbose_name='IAPassFail')),
                ('see_awarded', models.IntegerField(verbose_name='EndExamAwarded')),
                ('see_passfail', models.IntegerField(verbose_name='EndExamPassFail')),
                ('present_absent', models.IntegerField(verbose_name='PresentOrAbsent')),
                ('attempt', models.IntegerField(null=True, verbose_name='Attempt')),
                ('exam1', models.IntegerField(verbose_name='Exam1')),
                ('exam2', models.IntegerField(verbose_name='Exam2')),
                ('exam3', models.IntegerField(null=True, verbose_name='Exam3')),
                ('valuation3', models.IntegerField(verbose_name='Valuation3')),
                ('gracemarks', models.IntegerField(verbose_name='GraceMark')),
                ('grade', models.CharField(max_length=2, verbose_name='Grade')),
                ('attper', models.IntegerField(verbose_name='AttPer')),
                ('eligible', models.IntegerField(verbose_name='EndExamEligible')),
                ('nochange', models.IntegerField(null=True, verbose_name='NoChange')),
            ],
        ),
    ]