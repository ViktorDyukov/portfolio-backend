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
            'fields': ('id', 'title', 'tag', 'date'),
        }),
        ('Appearance', {
            'fields': ('bg_color', 'preview_deskX2'),
        }),
        ('Content 1', {
            'fields': ('c1_title', 'c1_body'),
        }),
        ('Content 2', {
            'fields': ('c2_title', 'c2_body'),
        }),
        ('Content 3', {
            'fields': ('c3_title', 'c3_body'),
        }),
        ('Content 4', {
            'fields': ('c4_title', 'c4_body'),
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
