# Generated by Django 5.0 on 2023-12-29 22:59

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("post", "0005_alter_reply_options"),
    ]

    operations = [
        migrations.RenameField(
            model_name="notification",
            old_name="context",
            new_name="content",
        ),
    ]