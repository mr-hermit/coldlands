from django.contrib import admin

from wsglobal.models import Site,SiteInfo,HitCount, Message
from navigation.models import NavItem

class SiteInfoInline(admin.StackedInline):
    model = SiteInfo
    fk_name = "site"

class NavItemInline(admin.StackedInline):
    model = NavItem
    fk_name = "site"

@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    inlines = [
        SiteInfoInline,
        NavItemInline,
    ]

@admin.register(HitCount)
class HitCountAdmin(admin.ModelAdmin):
    list_display = ('url','hits')


@admin.register(Message)
class MesaageAdmin(admin.ModelAdmin):
    pass