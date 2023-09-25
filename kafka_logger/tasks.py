from datetime import datetime, timedelta

from apps.kafka_logger.models import Log


def remove_log_error_tasks(days=15):
    date = datetime.now() - timedelta(days=days)
    logs = Log.objects.filter(date__lte=date, status=Log.FAILED)
    deleted_quantity = logs.count()
    for log in logs:
        log.delete()
    print(f"Foi deletado {deleted_quantity} logs")


def remove_log_success_tasks(days=1):
    date = datetime.now() - timedelta(days=days)
    logs = Log.objects.filter(date__lte=date, status=Log.SUCCESS)
    deleted_quantity = logs.count()
    for log in logs:
        log.delete()
    print(f"Foi deletado {deleted_quantity} logs que deram certo")
