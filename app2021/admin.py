from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from .models import Customisation, Case, Tag, Link, Page, CaseImage, CaseInfoSection

class ImageInline(SortableInlineAdminMixin, admin.StackedInline):
    model = CaseImage


class InfoInline(SortableInlineAdminMixin, admin.StackedInline):
    model = CaseInfoSection

class CaseAdmin(SortableAdminMixin, admin.ModelAdmin):
    readonly_fields = ('id',)
    fieldsets = (
        ('Main info', {
            'fields': ('id', 'title', 'tag', 'description'),
        }),
        ('Appearance', {
            'fields': ('bg_color', 'preview_deskX2'),
        })
    )
    inlines = [
        InfoInline, ImageInline
    ]


admin.site.register(Customisation)
admin.site.register(Link)
admin.site.register(Tag)
admin.site.register(Page)
admin.site.register(Case, CaseAdmin)
