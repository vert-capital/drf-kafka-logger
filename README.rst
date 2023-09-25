DRF kafka logger
=========================================


drf-kafka-logger is a app to generate logger in kafka consumer.


Quick start
-----------

1. Add "kafka_logger"  to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...,
        "kafka_logger",
    ]

2. How to use::

    from kafka_logger.utils import KafkaLogger

    # Init log
    logger = KafkaLogger()
    logger.init()

    # Set data
    logger.set_data(data:dict)

    # If success
    logger.success()

    # If error
    logger.error(error_message:str)



3. Run ``python manage.py migrate`` to create the drf-kafka-logger models.

4. <OPTIONAL> Tasks to clean log::

    from kafka_logger.tasks import remove_log_error_tasks, remove_log_success_tasks

    # In this example, it will delete logs with status success from the previous day
    remove_log_success_tasks(days=1)

    # In this example, it will delete logs with status error from the previous day
    remove_log_error_tasks(days=1)

    # I recommend using djangoQ Schedule
    # kafka_logger.tasks.remove_log_error_tasks
    # kafka_logger.tasks.remove_log_success_tasks