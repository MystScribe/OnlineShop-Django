from django.contrib import admin
from .models import product, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}
    list_display = ('name', 'is_sub')
    list_filter = ('is_sub', )

@admin.register(product)
class productAdmin(admin.ModelAdmin):
    raw_id_fields = ('category', )
    prepopulated_fields = {'slug': ('name', )}