from django.db import models
from django.utils.translation import ugettext_lazy as _


class Ministry(models.Model):
    name = models.CharField(_('Nombre'),
                            max_length=140)
    description = models.TextField(_('Descripción'), blank=True)
    contact = models.TextField(_('Datos de contacto'), blank=True)
    leader = models.ManyToManyField("accounts.Membership",
                                    verbose_name=_('Líder'),
                                    related_name="ministeries_leading")
    members = models.ManyToManyField("accounts.Membership",
                                     verbose_name=_('Miembros'),
                                     related_name="ministeries",
                                     blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Ministerio')
        verbose_name_plural = _('Ministerios')


DAY = (
    ('LU', _('Lunes')),
    ('MA', _('Martes')),
    ('MI', _('Miercoles')),
    ('JU', _('Jueves')),
    ('VI', _('Viernes')),
    ('SA', _('Sábado')),
    ('DO', _('Domingo')),
)


class Service(models.Model):
    name = models.CharField(_('Nombre'), max_length=140)
    description = models.TextField(_('Descripción'), blank=True)
    contact = models.TextField(_('Datos de contacto'), blank=True)
    leader = models.ManyToManyField("accounts.Membership",
                                    verbose_name=_('Líder'),
                                    related_name="service_leading")
    members = models.ManyToManyField("accounts.Membership",
                                     verbose_name=_('Miembros'),
                                     related_name="services",
                                     blank=True)
    day = models.CharField(_('Día'), max_length=140, choices=DAY,
                           blank=True, null=True)
    time = models.TimeField(_('Hora'), blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Servicio')
        verbose_name_plural = _('Servicios')


class Activity(models.Model):
    name = models.CharField(_('Nombre'), max_length=140)
    description = models.TextField(_('Descripción'), blank=True)
    contact = models.TextField(_('Datos de contacto'), blank=True)
    leader = models.ManyToManyField("accounts.Membership",
                                    verbose_name=_('Líder'),
                                    related_name="activity_leading")
    date = models.DateTimeField(_('Fecha de la actividad'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Actividad')
        verbose_name_plural = _('Actividades')


class DateContact(models.Model):
    address = models.TextField(_("Dirección"))
    email = models.TextField(_("Correos de contacto"))
    phone = models.TextField(_("Teléfono de contacto"))
    # image_map = models.ImageField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "contact {}".format(self.id)

    class Meta:
        verbose_name = _('Datos de contacto')
        verbose_name_plural = _('Datos de contacto')