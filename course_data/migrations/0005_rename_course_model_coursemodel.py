# Generated by Django 5.0.6 on 2024-06-29 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course_data', '0004_rename_branch_id_course_model_branch_id_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='course_Model',
            new_name='courseModel',
        ),
    ]