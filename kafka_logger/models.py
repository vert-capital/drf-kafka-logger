from uuid import uuid4 as guid

from django.contrib.contenttypes.models import ContentType
from django.db import models


class Log(models.Model):
    IN_PROGRESS = "in_progress"
    SUCCESS = "success"
    FAILED = "failed"
    STATUS_CHOICES = (
        (IN_PROGRESS, "Em progresso"),
        (SUCCESS, "Sucesso"),
        (FAILED, "Erro"),
    )
    id = models.UUIDField(primary_key=True, default=guid)
    content_type = models.ForeignKey(
        ContentType, on_delete=models.PROTECT, blank=True, null=True
    )
    date = models.DateTimeField(
        verbose_name="Data da operação",
        auto_now_add=True)
    status = models.CharField(
        verbose_name="Status", choices=STATUS_CHOICES, max_length=11
    )
    data = models.JSONField(
        verbose_name="Dados recebido",
        null=True,
        blank=True
    )
    error = models.TextField(
        verbose_name="Erro",
        null=True,
        blank=True)
    created_at = models.DateTimeField(
        verbose_name="Data de criação", auto_now_add=True)
    updated_at = models.DateTimeField(
        verbose_name="Data de atuaização", auto_now=True)

    class Meta:
        verbose_name = "Log do kafka"
        verbose_name_plural = "Logs do kafka"
