# Generated by Django 4.1 on 2022-10-30 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_1', '0008_alter_register1_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register1',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]