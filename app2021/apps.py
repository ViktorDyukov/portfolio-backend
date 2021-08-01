from django.apps import AppConfig

def store_as_webp(sender, **kwargs):
    webp_path = sender.storage.path('.'.join([sender.name, '.webp']))
    sender.image.save(webp_path, 'webp')


class App2021Config(AppConfig):
    name = 'app2021'

    def ready(self):
        from easy_thumbnails.signals import thumbnail_created
        thumbnail_created.connect(store_as_webp)