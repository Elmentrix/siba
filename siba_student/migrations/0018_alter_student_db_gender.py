# Generated by Django 4.1.7 on 2023-05-31 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siba_student', '0017_alter_student_db_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_db',
            name='gender',
            field=models.CharField(max_length=10),
        ),
    ]
