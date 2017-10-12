from __future__ import unicode_literals
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, AbstractUser
from django.db.models import signals
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
# Create your models here.


class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    phone = models.CharField(max_length=16, blank=True, null=True)
    recovery_code = models.CharField(max_length=16, blank=True, null=True)
    address = models.TextField(blank=True)
    membership = models.OneToOneField("accounts.Membership",
                                      blank=True, null=True,
                                      related_name="user")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def save(self, *args, **kwargs):
        self.username = self.email
        super(User, self).save()

    def __str__(self):
        return self.email


class Membership(models.Model):
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    email = models.EmailField(_('email address'), blank=True)
    is_active = models.BooleanField(
        _('active'),
        default=True,
    )
    birthday = models.DateField(blank=True, null=True)
    ci = models.IntegerField(null=True, blank=True)
    phone = models.TextField(blank=True)

    def get_full_name(self):
        if hasattr(self, "user"):
            return self.user.get_full_name()
        return "{0} {1}".format(self.first_name, self.last_name)

    def __str__(self):
        return self.get_full_name()