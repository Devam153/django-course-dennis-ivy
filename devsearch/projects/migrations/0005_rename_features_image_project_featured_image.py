# Generated by Django 4.2.7 on 2024-05-01 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_rename_demo_link_project_demo_link_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='features_image',
            new_name='featured_image',
        ),
    ]