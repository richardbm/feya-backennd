from django.contrib import admin
from accounts import models
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _
from jet.filters import RelatedFieldAjaxListFilter
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import Group
from jet.admin import CompactInline


class UserInline(CompactInline):
    model = models.User


class UserAdminExtend(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'membership')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups',
                   ('membership', RelatedFieldAjaxListFilter))
    search_fields = ('first_name', 'last_name', 'email')
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)


class MembershipAdmin(admin.ModelAdmin):
    inlines = (UserInline,)


admin.site.register(models.User, UserAdminExtend)
admin.site.register(models.Membership, MembershipAdmin)
# admin.site.unregister(Token)
# admin.site.unregister(Group)