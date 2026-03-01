from django.contrib import admin
from django.utils.html import format_html
from .models import AboutContent, PlusAbout, BlogAbout, Faq, Testimonials


@admin.register(AboutContent)
class AboutContentAdmin(admin.ModelAdmin):
    list_display = ("title", "big_image_preview", "autograph_preview")
    search_fields = ("title", "desc")
    readonly_fields = ("big_image_preview", "autograph_preview")

    fieldsets = (
        ("Основная информация", {
            "fields": ("title", "desc")
        }),
        ("Изображения", {
            "fields": ("big_img", "big_image_preview", "autograph_img", "autograph_preview")
        }),
    )

    def big_image_preview(self, obj):
        if obj.big_img:
            return format_html('<img src="{}" width="100"/>', obj.big_img.url)
        return "-"
    big_image_preview.short_description = "Превью большого фото"

    def autograph_preview(self, obj):
        if obj.autograph_img:
            return format_html('<img src="{}" width="100"/>', obj.autograph_img.url)
        return "-"
    autograph_preview.short_description = "Превью подписи"
    
    
@admin.register(PlusAbout)
class PlusAboutAdmin(admin.ModelAdmin):
    list_display = ("title", "image_preview")
    search_fields = ("title",)
    readonly_fields = ("image_preview",)

    def image_preview(self, obj):
        if obj.img:
            return format_html('<img src="{}" width="80"/>', obj.img.url)
        return "-"
    image_preview.short_description = "Превью"
    

@admin.register(BlogAbout)
class BlogAboutAdmin(admin.ModelAdmin):
    list_display = ("title", "image_preview")
    search_fields = ("title",)
    readonly_fields = ("image_preview",)

    def image_preview(self, obj):
        if obj.img:
            return format_html('<img src="{}" width="80"/>', obj.img.url)
        return "-"
    image_preview.short_description = "Превью"
    

@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title", "desc")
    
    
@admin.register(Testimonials)
class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ("name", "position", "avatar_preview")
    search_fields = ("name", "position")
    readonly_fields = ("avatar_preview",)

    def avatar_preview(self, obj):
        if obj.avatar:
            return format_html('<img src="{}" width="80"/>', obj.avatar.url)
        return "-"
    avatar_preview.short_description = "Аватар"
    
    
