# Generated by Django 4.1.7 on 2023-05-20 11:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('siba_student', '0003_student_db_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_db',
            name='upload_Result',
            field=models.FileField(default=django.utils.timezone.now, upload_to='file/'),
            preserve_default=False,
        ),
    ]