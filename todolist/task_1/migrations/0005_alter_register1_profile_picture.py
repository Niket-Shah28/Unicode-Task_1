# Generated by Django 4.1 on 2022-10-28 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_1', '0004_alter_register1_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register1',
            name='profile_picture',
            field=models.ImageField(default='images/Presentation2.jpg', upload_to='images/'),
        ),
    ]
