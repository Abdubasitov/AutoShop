from django.db import models
from django.utils.text import slugify

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    category = models.CharField(max_length=100, blank=True)  # например "eCommerce"
    image = models.ImageField(upload_to='blog/')
    excerpt = models.TextField(blank=True, help_text="Краткое описание поста")
    content = models.TextField()
    published_at = models.DateField(auto_now_add=True, null=True, blank=True)

    class Meta:
        ordering = ['-published_at']
        verbose_name = 'Блог пост'
        verbose_name_plural = 'Блог посты'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
