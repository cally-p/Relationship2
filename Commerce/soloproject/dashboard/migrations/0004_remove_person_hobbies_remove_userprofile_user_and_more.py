# Generated by Django 4.2.3 on 2023-08-10 22:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_userprofile_bio_userprofile_profile_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='hobbies',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='usersettings',
            name='user_profile',
        ),
        migrations.DeleteModel(
            name='Hobby',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
        migrations.DeleteModel(
            name='UserSettings',
        ),
    ]