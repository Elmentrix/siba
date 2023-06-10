# Generated by Django 4.1.7 on 2023-05-30 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siba_student', '0012_alter_student_db_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_db',
            name='age',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='student_db',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=200),
        ),
    ]
