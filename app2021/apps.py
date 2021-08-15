from django.apps import AppConfig
import subprocess
from django_cleanup.signals import cleanup_pre_delete
from django.conf import settings


def webp_create(sender, **kwargs):
    path = sender.storage.path(sender.name)
    webp_path = sender.storage.path('.'.join([sender.name, 'webp']))

    #creating webp
    batcmd = ["cwebp", "-preset", "photo", "-q", "75", path, "-o", webp_path]
    r = subprocess.call(batcmd)

    #optimizing png
    batcmd = ["pngquant", "-o", path, "--force", "--quality=70-80", path]

    r = subprocess.call(batcmd)


def webp_delete(**kwargs):
    path = kwargs['file'].name.split("/", 1)
    full_path = "/".join([settings.MEDIA_ROOT, path[0]])
    pattern = path[1] + "*_crop.png.webp"
    batcmd = ["find", full_path, "-type", "f", "-name", pattern, "-delete"]
    r = subprocess.call(batcmd)
    print(full_path)
    print(pattern)




class App2021Config(AppConfig):
    name = 'app2021'

    def ready(self):
        from easy_thumbnails.signals import thumbnail_created
        thumbnail_created.connect(webp_create)
        cleanup_pre_delete.connect(webp_delete)



