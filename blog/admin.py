from django.contrib import admin
from blog import models
from django.utils.translation import ugettext_lazy as _


class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'categories_names', 'date')
    list_filter = ('owner', 'categories')
    search_fields = ('title', 'owner__first_name', 'owner__last_name',
                     'owner__email', 'categories__name')
    ordering = ('title', 'owner', 'categories__name', 'date')

    def categories_names(self, obj):
        names = ", ".join([ins.name for ins in obj.categories.all()])
        return names

    categories_names.short_description = _("Categorías")


admin.site.register(models.Category)
admin.site.register(models.Publication, PublicationAdmin)
