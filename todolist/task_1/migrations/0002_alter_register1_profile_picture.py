# Generated by Django 4.1 on 2022-10-27 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register1',
            name='profile_picture',
            field=models.ImageField(default='<img src="default_image/Presentation2.jpg">', upload_to='media/images'),
        ),
    ]
