import os

from django.db.models import signals
from django.dispatch import receiver

from app.models import HotelPhoto


@receiver(signals.pre_delete, sender=HotelPhoto, weak=False)
def delete_image(sender, instance, **kwargs):
    dir_name = os.path.dirname(instance.photo.path)
    file_name = os.path.basename(instance.photo.path)

    os.remove(dir_name + '\\' + file_name)
