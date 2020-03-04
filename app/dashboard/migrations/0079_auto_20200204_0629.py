# Generated by Django 2.2.4 on 2020-02-04 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0078_profile_as_representation'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='tribe_priority',
            field=models.TextField(blank=True, default='', help_text='HTML rich description for what tribe priorities.'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='tribe_description',
            field=models.TextField(blank=True, default='', help_text='HTML rich description describing tribe.'),
        ),
    ]