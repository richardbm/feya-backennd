from __future__ import unicode_literals
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, AbstractUser
from django.db.models import signals
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from accounts.utils import send_email
from django.db.models import deletion


class User(AbstractUser):
    email = models.EmailField(_('Correo electrónico'), unique=True)
    phone = models.CharField(_('Teléfono'), max_length=16, blank=True, null=True)
    recovery_code = models.CharField(max_length=16, blank=True, null=True)
    address = models.TextField(_('Dirección'), blank=True)
    membership = models.OneToOneField("accounts.Membership",
                                      verbose_name=_('Membresía'),
                                      blank=True, null=True,
                                      related_name="user",
                                      on_delete=deletion.SET_NULL)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def save(self, *args, **kwargs):
        self.username = self.email
        super(User, self).save()

    def __str__(self):
        return self.get_full_name()

    @staticmethod
    def autocomplete_search_fields():
        return 'membership',

    class Meta:
        verbose_name = _('Usuario')
        verbose_name_plural = _('Usuarios')


class Membership(models.Model):
    first_name = models.CharField(_('Nombres'), max_length=30, blank=True)
    last_name = models.CharField(_('Apellidos'), max_length=30, blank=True)
    email = models.EmailField(_('Correo electrónico'), blank=True)
    address = models.TextField(_('Dirección'), blank=True)
    is_active = models.BooleanField(
        _('Miembro activo'),
        default=True,
    )
    birthday = models.DateField(_('Cumpleaños'),
                                blank=True, null=True)
    ci = models.IntegerField(_('Cédula de identidad'),
                             null=True, blank=True)
    phone = models.TextField(_('Teléfonos'), blank=True)
    is_baptized = models.BooleanField(_('Es bautizado'))

    def get_full_name(self):
        if hasattr(self, "user"):
            return self.user.get_full_name()
        return "{0} {1}".format(self.first_name, self.last_name)

    def __str__(self):
        return self.get_full_name()

    class Meta:
        verbose_name = _('Miembro')
        verbose_name_plural = _('Miembros')


def send_invitation_email(sender, instance, created=None, **kwargs):
    if created and instance.email:
        # TODO: cambiar template por uno personalizado
        template = 'email/email_invitation.html'
        email_destinity = instance.email
        subject = "Registrate en nuestra  plataforma online"

        msg = "Hola {0}.\n\n La iglesia Fe, esperaza y amor te invita a" \
                  " registrarte en nuestra plataforma online." \
              "\n\nDios te bendiga".format(instance.get_full_name())
        data = {
            "msg": msg
        }
        send_email(template, email_destinity, subject, data)



signals.post_save.connect(send_invitation_email, sender=Membership)
