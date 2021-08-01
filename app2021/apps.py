from django.apps import AppConfig
import logging
logger = logging.getLogger(__file__)

def store_as_webp(sender, **kwargs):
    logger.error("111")
    webp_path = sender.storage.path('.'.join([sender.name, 'webp_test']))
    sender.image.save(webp_path, 'png')
    logger.error("222")


class App2021Config(AppConfig):
    name = 'app2021'

    def ready(self):
        logger.error("222333")
        from easy_thumbnails.signals import thumbnail_created
        thumbnail_created.connect(store_as_webp)