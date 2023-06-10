# Generated by Django 4.1.7 on 2023-05-20 08:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('siba_student', '0002_remove_student_db_gender_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_db',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female')], default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
    ]