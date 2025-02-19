from django.contrib import admin
from site_setup.models import MenuLink, SiteSetup

# @admin.register(MenuLink)
# class MenuLinkAdmin(admin.ModelAdmin):
#     list_display = 'text', 'url_or_path', 'id',
#     list_display_links = 'text', 'url_or_path', 'id',
#     search_fields = 'text', 'url_or_path', 'id',

class MenuLinkInline(admin.TabularInline):
    model = MenuLink
    extra = 1

@admin.register(SiteSetup)
class SiteSetupAdmin(admin.ModelAdmin):
    list_display = 'title', 'description',
    inlines = MenuLinkInline,

    def has_add_permission(self, request):
        return not SiteSetup.objects.exists() 

