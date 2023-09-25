DRF kafka logger
=========================================


DRF-kafka-logger is a app to generate logger in kafka consumer.


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
    logger.data(data:dict)

    # If success
    logger.success()

    # If error
    logger.error(error_message:str)



3. Run ``python manage.py migrate`` to create the drf_cas_jwt models.