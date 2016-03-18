from django.contrib import admin
from navigation.models import NavItem, NavItemNested

class NavSubItemInline(admin.TabularInline):
    model = NavItemNested
    fk_name = "parent"

@admin.register(NavItem)
class NavItemAdmin(admin.ModelAdmin):
    inlines = [
        NavSubItemInline
    ]

