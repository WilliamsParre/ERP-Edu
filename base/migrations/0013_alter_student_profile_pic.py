# Generated by Django 4.0.4 on 2022-05-10 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_alter_course_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='base/static/images'),
        ),
    ]
