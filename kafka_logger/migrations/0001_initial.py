# Generated by Django 3.2.8 on 2023-04-20 16:19

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Log",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                (
                    "date",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Data da operação"
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("in_progress", "Em progresso"),
                            ("success", "Sucesso"),
                            ("failed", "Erro"),
                        ],
                        max_length=11,
                        verbose_name="Status",
                    ),
                ),
                (
                    "data",
                    models.JSONField(
                        blank=True, null=True, verbose_name="Dados recebido"
                    ),
                ),
                ("error", models.TextField(blank=True, null=True, verbose_name="Erro")),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Data de criação"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Data de atuaização"
                    ),
                ),
            ],
            options={
                "verbose_name": "Log do kafka",
                "verbose_name_plural": "Logs do kafka",
            },
        ),
    ]
