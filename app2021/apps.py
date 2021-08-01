from django.apps import AppConfig

def store_as_webp(sender, **kwargs):
    print("111")
    webp_path = sender.storage.path('.'.join([sender.name, 'webp_test']))
    sender.image.save(webp_path, 'png')
    print("222")


class App2021Config(AppConfig):
    name = 'app2021'

    def ready(self):
        from easy_thumbnails.signals import thumbnail_created
        thumbnail_created.connect(store_as_webp)