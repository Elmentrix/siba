# Generated by Django 4.1.7 on 2023-05-23 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siba_student', '0005_remove_student_db_upload_result'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student_db',
            name='id',
        ),
        migrations.AlterField(
            model_name='student_db',
            name='student_Id',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
