# Generated by Django 4.0.1 on 2022-02-01 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_age_student_studentage_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='track_name',
            new_name='trackname',
        ),
        migrations.AlterField(
            model_name='student',
            name='studentage',
            field=models.IntegerField(),
        ),
    ]