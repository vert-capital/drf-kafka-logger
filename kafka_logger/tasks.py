from datetime import datetime, timedelta

from apps.kafka_logger.models import Log


def remove_log_error_tasks():
    date = datetime.now() - timedelta(days=15)
    logs = Log.objects.filter(date__lte=date, status=Log.FAILED)
    deleted_quantity = logs.count()
    for log in logs:
        log.delete()
    print(f"Foi deletado {deleted_quantity} logs")


def remove_log_success_tasks():
    date = datetime.now() - timedelta(days=1)
    logs = Log.objects.filter(date__lte=date, status=Log.SUCCESS)
    deleted_quantity = logs.count()
    for log in logs:
        log.delete()
    print(f"Foi deletado {deleted_quantity} logs que deram certo")
