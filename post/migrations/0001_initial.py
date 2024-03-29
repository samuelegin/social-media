# Generated by Django 5.0 on 2023-12-28 14:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "post_image",
                    models.ImageField(blank=True, null=True, upload_to="post_image"),
                ),
                ("caption", models.CharField(blank=True, max_length=3000, null=True)),
                ("date_posted", models.DateTimeField(auto_now_add=True)),
                (
                    "post_owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="post_owner",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-date_posted"],
            },
        ),
    ]
