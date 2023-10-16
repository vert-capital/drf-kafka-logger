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
    logger.init(Model)

    # Set data
    logger.set_data(data:dict)

    # If success
    logger.success()

    # If error
    logger.error(message_error:str)



3. Run ``python manage.py migrate`` to create the drf-kafka-logger models.

4. <OPTIONAL> Tasks to clean log::

    from kafka_logger.tasks import remove_generic_status

    # In this example, it will delete logs with status success from the previous day
    remove_generic_status(days=1, status="success")

    # In this example, it will delete logs with status error from the previous day
    remove_generic_status(days=1, status="failed)

    # I recommend using djangoQ Schedule
    # kafka_logger.tasks.remove_generic_status
