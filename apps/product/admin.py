from django.contrib import admin
from .models import (
    Category,
    Brand,
    Product,
    ProductImage,
    Attribute,
    AttributeValue,
    ProductVariant,
    Review
)
from django.contrib import admin

admin.site.index_title = "Добро пожаловать"

# CATEGORY

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "parent", "is_active")
    search_fields = ("name",)
    list_filter = ("is_active",)
    prepopulated_fields = {"slug": ("name",)}


# BRAND

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}


# INLINES FOR PRODUCT
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 2

class ProductVariantInline(admin.TabularInline):
    model = ProductVariant
    extra = 1
    filter_horizontal = ("attributes",)


# PRODUCT

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "stock", "is_available")
    list_filter = ("is_available", "category")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}

    fieldsets = (
        ("Основная информация", {
            "fields": ("name", "slug", "category", "brand")
        }),
        ("", {
            "fields": ("description",)
        }),
        ("", {
            "fields": ("price", "stock", "is_available")
        }),
    )

    inlines = [
        ProductImageInline,
        ProductVariantInline,
    ]


# ATTRIBUTE

class AttributeValueInline(admin.TabularInline):
    model = AttributeValue
    extra = 1


@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    inlines = [AttributeValueInline]


# REVIEW

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("product", "user", "reiting", "created_at")
    list_filter = ("reiting",)
    search_fields = ("product__name", "user__username")