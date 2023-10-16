from datetime import datetime, timedelta

from .models import Log


def remove_generic_status(days=1, status="success"):
    date = datetime.now() - timedelta(days=days)
    logs = Log.objects.filter(date__lte=date, status=status)
    deleted_quantity = logs.count()
    for log in logs:
        log.delete()
    print(f"Foi deletado {deleted_quantity} logs do status", status)
