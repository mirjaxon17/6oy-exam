from django.contrib import admin
from .models import Types, Product, Testiminial, Bonus, Organic
from import_export.admin import ImportExportModelAdmin




@admin.register(Types)
class TypesAdmin(ImportExportModelAdmin):
    list_display = ("id", 'types', 'image')
    list_display_links = ("id", 'types', 'image')
    search_fields = ('types',"id")
    ordering = ("id",)

@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    list_display = ('id', 'title', 'description', 'price')
    list_display_links = ('id', 'title', 'description', 'price')
    search_fields = ('title', 'price', 'description')
    ordering = ('id',)


@admin.register(Bonus)
class BonusAdmin(ImportExportModelAdmin):
    pass

@admin.register(Organic)
class OrganicAdmin(ImportExportModelAdmin):
    pass



@admin.register(Testiminial)
class TestiminialAdmin(ImportExportModelAdmin):
    list_display = ('id', 'last_name', 'first_name',  'description', 'profession')
    list_display_links = ('id', 'last_name', 'first_name', 'description', 'profession')
    search_fields = ('last_name','first_name', 'profession')
    ordering = ('last_name',)
