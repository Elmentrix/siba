# Generated by Django 4.1.7 on 2023-05-20 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siba_student', '0004_student_db_upload_result'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student_db',
            name='upload_Result',
        ),
    ]
