from datetime import datetime, timedelta

from django.db import connection
from django.utils import timezone


def remove_generic_status(days=1, status="success"):
    date = timezone.now() - timedelta(days=days)
    date = datetime(
        year=date.year, month=date.month, day=date.day, hour=0, minute=0, second=1
    )
    sql = """
        DELETE FROM kafka_logger_log as log
        WHERE
        log.status='{status}' AND
        log.date < '{date}'
    """.format(
        status=status, date=str(date)
    )
    with connection.cursor() as cursor:
        cursor.execute(sql)
    print("Tarefa finalizada")
