from django.contrib import admin
from ministry import models
# Register your models here.


class MinistryAdmin(admin.ModelAdmin):
    list_display = ('name', 'leader_names')
    list_filter = ('leader',)
    search_fields = ('name', 'leader__first_name', 'leader__last_name',
                     'leader__email',)
    ordering = ('name', 'leader')

    def leader_names(self, obj):
        names = ", ".join([ins.get_full_name() for ins in obj.leader.all()])
        return names

    leader_names.short_description = 'Líder'


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'leader_names', 'day', 'time')
    list_filter = ('leader',)
    search_fields = ('name', 'leader__first_name', 'leader__last_name',
                     'leader__email',)
    ordering = ('name', 'day', 'time', 'leader')

    def leader_names(self, obj):
        names = ", ".join([ins.get_full_name() for ins in obj.leader.all()])
        return names

    leader_names.short_description = 'Líder'


class ActivityAdmin(admin.ModelAdmin):
    # TODO: Agregar django-adin-rangefilter
    list_display = ('name', 'leader_names', 'date')
    list_filter = ('leader',)
    search_fields = ('name', 'leader__first_name', 'leader__last_name',
                     'leader__email',)
    ordering = ('name', 'date', 'leader')

    def leader_names(self, obj):
        names = ", ".join([ins.get_full_name() for ins in obj.leader.all()])
        return names

    leader_names.short_description = 'Líder'


class DateContactAdmin(admin.ModelAdmin):
    list_display = ('address', 'phone', 'date')
    search_fields = ('address', 'phone', 'email')
    ordering = ('date',)


admin.site.register(models.Ministry, MinistryAdmin)
admin.site.register(models.Service, ServiceAdmin)
admin.site.register(models.Activity, ActivityAdmin)
admin.site.register(models.DateContact, DateContactAdmin)
