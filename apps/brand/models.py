from django.db import models
from django.utils.text import slugify


class Brand(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, blank=True)
    logo = models.ImageField(upload_to='brands/')
    created_at = models.DateTimeField(auto_now_add=True)
    website = models.URLField(
        blank=True,
        null=True,
        help_text="Ссылка на сайт бренда или страницу бренда"
    )
    class Meta:
        ordering = ['name']
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name