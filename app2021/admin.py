from django.contrib import admin
from .models import Customisation, Project, Skill, Page, Link, ProjectAdmin, PageAdmin


admin.site.register(Customisation)
admin.site.register(Link)
admin.site.register(Skill)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Page, PageAdmin)


