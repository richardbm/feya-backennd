from django.db import models
from django.utils.translation import ugettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField


class Category(models.Model):
    name = models.CharField(_('Nombre'), max_length=140)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Categoría')
        verbose_name_plural = _('Categorías')


class Publication(models.Model):
    title = models.CharField(_('Título'), max_length=140)
    text = RichTextUploadingField(_('Contenido'))
    date = models.DateTimeField(_('Fecha de creación'),
                                auto_now_add=True)
    categories = models.ManyToManyField('blog.Category',
                                        verbose_name=_('Categorías'))
    owner = models.ForeignKey('accounts.User',
                              verbose_name=_('Creado por'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Publicación')
        verbose_name_plural = _('Publicaciones')
