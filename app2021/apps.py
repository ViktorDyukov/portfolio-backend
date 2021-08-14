from django.apps import AppConfig
import subprocess
import xml.etree.cElementTree as et


def store_as_webp(sender, **kwargs):
    path = sender.storage.path(sender.name)
    webp_path = sender.storage.path('.'.join([sender.name, 'webp']))

    #creating webp
    batcmd = "cwebp -preset photo -q 75 {} -o {}".format(path, webp_path)
    r = subprocess.Popen(batcmd, shell=True)

    #optimizing png
    batcmd = "pngquant -o {} --force --quality=70-80 {}".format(path, path)
    r = subprocess.Popen(batcmd, shell=True)




class App2021Config(AppConfig):
    name = 'app2021'

    def ready(self):
        from easy_thumbnails.signals import thumbnail_created
        thumbnail_created.connect(store_as_webp)
