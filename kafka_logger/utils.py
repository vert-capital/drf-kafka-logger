from django.contrib.contenttypes.models import ContentType

from .models import Log


class KafkaLogger:
    def __init__(self) -> None:
        self.object: Log = None

    def init(self, Model):
        obj = Model()
        content_type = ContentType.objects.get_for_model(obj)
        self.object = Log.objects.create(
            status=Log.IN_PROGRESS,
            content_type=content_type,
        )

    def set_data(self, data: dict):
        if type(data) == dict:
            self.object.data = data
            self.object.save()
            return
        raise TypeError("Data must be a dict")

    def success(self):
        self.object.status = Log.SUCCESS
        self.object.save()

    def error(self, message_error: str):
        self.object.status = Log.FAILED
        self.object.error = message_error
        self.object.save()
