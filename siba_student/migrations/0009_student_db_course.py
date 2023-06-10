# Generated by Django 4.1.7 on 2023-05-26 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('siba_admin', '0003_assignments'),
        ('siba_student', '0008_remove_student_db_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_db',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='siba_admin.courses'),
        ),
    ]