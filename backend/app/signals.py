import os

from django.db.models import signals
from django.dispatch import receiver
from django.contrib.auth import get_user_model

from app.models import HotelPhoto, Tourist


@receiver(signals.pre_delete, sender=HotelPhoto, weak=False)
def delete_image(sender, instance, **kwargs):
    dir_name = os.path.dirname(instance.photo.path)
    file_name = os.path.basename(instance.photo.path)

    if os.path.exists(os.path.join(dir_name, file_name)):
        os.remove(dir_name + '/' + file_name)


@receiver(signals.post_delete, sender=Tourist, weak=False)
def delete_document(sender, instance, **kwargs):
    if not get_user_model().objects.filter(document=instance.document):
        instance.document.delete()


