# Generated by Django 4.1.6 on 2023-03-02 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company_files', '0003_alter_user_email_alter_user_first_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='name',
            new_name='file',
        ),
    ]